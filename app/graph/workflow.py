from langgraph.graph import StateGraph, END
from app.graph.state import GPIEGraphState
from app.graph.nodes import (
    ingest_node,
    classify_intent_node,
    extract_product_node,
    offer_discovery_node,
    policy_check_node,
    outreach_node
)
from app.graph.edges import (
    check_intent_qualification,
    check_offers_exist,
    check_policy_approval
)

def build_gpie_workflow():
    workflow = StateGraph(GPIEGraphState)

    workflow.add_node("ingest", ingest_node)
    workflow.add_node("classify_intent", classify_intent_node)
    workflow.add_node("extract_product", extract_product_node)
    workflow.add_node("offer_discovery", offer_discovery_node)
    workflow.add_node("policy_check", policy_check_node)
    workflow.add_node("outreach", outreach_node)

    workflow.set_entry_point("ingest")
    workflow.add_edge("ingest", "classify_intent")

    workflow.add_conditional_edges(
        "classify_intent",
        check_intent_qualification,
        {
            "QUALIFIED": "extract_product",
            "DISQUALIFIED": END
        }
    )

    workflow.add_edge("extract_product", "offer_discovery")

    workflow.add_conditional_edges(
        "offer_discovery",
        check_offers_exist,
        {
            "OFFER_EXISTS": "policy_check",
            "NO_OFFER": END
        }
    )

    workflow.add_conditional_edges(
        "policy_check",
        check_policy_approval,
        {
            "APPROVED": "outreach",
            "DENIED": END
        }
    )

    workflow.add_edge("outreach", END)

    return workflow.compile()

gpie_graph = build_gpie_workflow()
