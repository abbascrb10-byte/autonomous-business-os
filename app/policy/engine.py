from app.domain.signals import DemandSignal
from app.domain.offers import Offer

class PolicyEngine:
    ALLOWED_SOURCES = ["requests", "forums", "search", "owned", "agentic"]

    @classmethod
    def evaluate(cls, signal: DemandSignal, offer: Offer) -> bool:
        if signal.source not in cls.ALLOWED_SOURCES:
            return False

        # Policy: Must be in stock and have affiliate URL
        if not offer.in_stock or not offer.affiliate_url:
            return False

        return True
