import re
from app.domain.signals import DemandSignal
from app.domain.intents import PurchaseIntent, ExtractedProductRequirements

class IntentAgent:
    @staticmethod
    def classify_intent(signal: DemandSignal) -> PurchaseIntent:
        text = signal.raw_text.lower()
        score = 0.0

        keywords = ["need", "looking to buy", "where can i buy", "where to buy", "best place to buy", "under $", "price", "shipped to"]
        for kw in keywords:
            if kw in text:
                score += 20.0

        if re.search(r"\$\d+", text) or re.search(r"\b\d+\s*(usd|eur|gbp|\$)\b", text):
            score += 20.0

        intent_score = min(score, 100.0)
        req = ExtractedProductRequirements()

        return PurchaseIntent(
            signal_id=signal.signal_id or "temp_sig_id",
            intent_score=intent_score,
            requirements=req,
            qualified=(intent_score >= 40.0)
        )
