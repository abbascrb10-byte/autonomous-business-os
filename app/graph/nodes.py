from app.graph.state import GPIEGraphState
from app.agents.intent_agent import IntentAgent
from app.agents.product_agent import ProductAgent
from app.agents.offer_agent import OfferAgent
from app.agents.ranking_agent import RankingAgent
from app.policy.engine import PolicyEngine
from app.outreach.dispatcher import TwoMessageOutreachDispatcher
from app.domain.contacts import Contact

async def ingest_node(state: GPIEGraphState) -> GPIEGraphState:
    state["status"] = "SIGNAL_INGESTED"
    return state

async def classify_intent_node(state: GPIEGraphState) -> GPIEGraphState:
    intent = IntentAgent.classify_intent(state["signal"])
    state["intent"] = intent
    state["status"] = "INTENT_CLASSIFIED" if intent.qualified else "INTENT_DISQUALIFIED"
    return state

async def extract_product_node(state: GPIEGraphState) -> GPIEGraphState:
    reqs = ProductAgent.extract_requirements(state["signal"])
    state["requirements"] = reqs
    if state["intent"]:
        state["intent"].requirements = reqs
    state["status"] = "REQUIREMENTS_EXTRACTED"
    return state

async def offer_discovery_node(state: GPIEGraphState) -> GPIEGraphState:
    if not state["requirements"]:
        state["offers"] = []
        return state

    offer_agent = OfferAgent()
    offers = await offer_agent.search_all_merchants(state["requirements"])
    ranked = RankingAgent.rank_offers(offers, state["requirements"])

    state["offers"] = ranked
    state["best_offer"] = ranked[0] if ranked else None
    state["status"] = "OFFERS_RANKED" if ranked else "NO_OFFERS_FOUND"
    return state

async def policy_check_node(state: GPIEGraphState) -> GPIEGraphState:
    if not state["best_offer"]:
        state["policy_allowed"] = False
        state["status"] = "POLICY_DENIED"
        return state

    allowed = PolicyEngine.evaluate(state["signal"], state["best_offer"])
    state["policy_allowed"] = allowed
    state["status"] = "POLICY_ALLOWED" if allowed else "POLICY_DENIED"
    return state

async def outreach_node(state: GPIEGraphState) -> GPIEGraphState:
    if not state["policy_allowed"] or not state["best_offer"]:
        state["status"] = "OUTREACH_SKIPPED"
        return state

    contact = Contact(
        source=state["signal"].source,
        author_reference=state["signal"].author_reference or "anon",
        channel="direct_message"
    )
    state["contact"] = contact

    intent_id = (state["intent"].intent_id if state.get("intent") and state["intent"].intent_id else "intent_temp")

    perm_msg = TwoMessageOutreachDispatcher.create_permission_request(intent_id, contact, state["best_offer"])
    state["permission_message"] = perm_msg

    if state.get("user_response", "").strip().lower() == "yes":
        contact.permission_granted = True
        comm_msg = TwoMessageOutreachDispatcher.create_commercial_offer(intent_id, contact, state["best_offer"])
        state["offer_message"] = comm_msg
        state["status"] = "COMMERCIAL_OFFER_SENT"
    else:
        state["status"] = "PERMISSION_REQUEST_SENT"

    return state
