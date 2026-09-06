from typing import List
from app.domain.offers import Offer
from app.domain.intents import ExtractedProductRequirements

class RankingAgent:
    @staticmethod
    def rank_offers(offers: List[Offer], requirements: ExtractedProductRequirements) -> List[Offer]:
        for offer in offers:
            score = 100.0

            # Budget match
            if requirements.budget and offer.price > requirements.budget:
                score -= 30.0

            # Rating weight
            if offer.rating:
                score += offer.rating * 5.0

            # Commission balancing
            score += offer.commission_rate * 100.0

            offer.rank_score = round(score, 2)

        return sorted(offers, key=lambda o: o.rank_score or 0.0, reverse=True)
