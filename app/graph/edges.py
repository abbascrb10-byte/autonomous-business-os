from app.graph.state import GPIEGraphState

def check_intent_qualification(state: GPIEGraphState) -> str:
    if state["intent"] and state["intent"].qualified:
        return "QUALIFIED"
    return "DISQUALIFIED"

def check_offers_exist(state: GPIEGraphState) -> str:
    if state.get("best_offer"):
        return "OFFER_EXISTS"
    return "NO_OFFER"

def check_policy_approval(state: GPIEGraphState) -> str:
    if state.get("policy_allowed"):
        return "APPROVED"
    return "DENIED"
