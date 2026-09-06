import pytest
from app.domain.signals import DemandSignal
from app.domain.intents import PurchaseIntent, ExtractedProductRequirements
from app.agents.intent_agent import IntentAgent
from app.agents.product_agent import ProductAgent
from app.agents.ranking_agent import RankingAgent
from app.policy.engine import PolicyEngine
from app.merchants.amazon import AmazonAdapter
from app.merchants.ebay import EBayAdapter

def test_intent_classification():
    sig = DemandSignal(source="requests", source_id="t1", raw_text="I need to buy a laptop under $1000")
    intent = IntentAgent.classify_intent(sig)
    assert intent.qualified is True
    assert intent.intent_score >= 40.0

def test_product_requirement_extraction():
    sig = DemandSignal(source="requests", source_id="t2", raw_text="I need Sony Headphones under $300")
    reqs = ProductAgent.extract_requirements(sig)
    assert reqs.budget == 300.0
    assert "sony headphones" in reqs.product_name.lower()

@pytest.mark.asyncio
async def test_merchant_adapters_and_ranking():
    reqs = ExtractedProductRequirements(product_name="Sony Camera", budget=1500.0)
    amz = AmazonAdapter()
    ebay = EBayAdapter()

    amz_offers = await amz.search_offers(reqs)
    ebay_offers = await ebay.search_offers(reqs)

    all_offers = amz_offers + ebay_offers
    assert len(all_offers) == 2

    ranked = RankingAgent.rank_offers(all_offers, reqs)
    assert len(ranked) == 2
    assert ranked[0].rank_score >= ranked[1].rank_score

def test_policy_engine():
    sig = DemandSignal(source="requests", source_id="t3", raw_text="Need item")
    reqs = ExtractedProductRequirements(product_name="Item")
    amz = AmazonAdapter()

    # Valid offer
    off = amz.search_offers
    # Test Policy Engine directly with valid offer
    from app.domain.offers import Offer
    valid_offer = Offer(product_id="p1", merchant="Amazon", title="Title", price=100.0, affiliate_url="http://amz.com")
    assert PolicyEngine.evaluate(sig, valid_offer) is True
