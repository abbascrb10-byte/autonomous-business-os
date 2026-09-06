import re
from app.domain.signals import DemandSignal
from app.domain.intents import ExtractedProductRequirements

class ProductAgent:
    @staticmethod
    def extract_requirements(signal: DemandSignal) -> ExtractedProductRequirements:
        text = signal.raw_text

        budget = None
        match = re.search(r"\$(\d+(?:\.\d{2})?)", text)
        if match:
            budget = float(match.group(1))

        product_name = text
        if "under $" in text.lower():
            product_name = text.lower().split("under $")[0].strip()
        elif "looking for" in text.lower():
            product_name = text.lower().split("looking for")[1].strip()

        return ExtractedProductRequirements(
            product_name=product_name or "General Item",
            budget=budget,
            currency="USD",
            destination_country=signal.country or "US"
        )
