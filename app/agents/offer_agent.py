from typing import List
from app.merchants.amazon import AmazonAdapter
from app.merchants.ebay import EBayAdapter
from app.domain.offers import Offer
from app.domain.intents import ExtractedProductRequirements

class OfferAgent:
    def __init__(self):
        self.adapters = [AmazonAdapter(), EBayAdapter()]

    async def search_all_merchants(self, requirements: ExtractedProductRequirements) -> List[Offer]:
        offers: List[Offer] = []
        for adapter in self.adapters:
            m_offers = await adapter.search_offers(requirements)
            offers.extend(m_offers)
        return offers
