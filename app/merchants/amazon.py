import uuid
from typing import List
from app.merchants.base import BaseMerchantAdapter
from app.domain.offers import Offer
from app.domain.intents import ExtractedProductRequirements
from app.config.settings import settings

class AmazonAdapter(BaseMerchantAdapter):
    def __init__(self):
        super().__init__(merchant_name="Amazon")
        self.associates_tag = settings.AMAZON_ASSOCIATES_TAG or "gpie-20"

    async def search_offers(self, requirements: ExtractedProductRequirements) -> List[Offer]:
        product_name = requirements.product_name or "Item"
        price = requirements.budget or 199.99
        product_id = f"prod_amz_{uuid.uuid4().hex[:8]}"

        affiliate_url = f"https://www.amazon.com/dp/B0EXAMPL3?tag={self.associates_tag}"

        return [
            Offer(
                offer_id=f"off_amz_{uuid.uuid4().hex[:8]}",
                product_id=product_id,
                merchant=self.merchant_name,
                title=f"{product_name} - Official Amazon Store",
                price=round(price * 0.95, 2),
                currency=requirements.currency or "USD",
                in_stock=True,
                seller="Amazon.com",
                shipping_destination=requirements.destination_country or "US",
                shipping_cost=0.0,
                rating=4.7,
                affiliate_url=affiliate_url,
                commission_rate=0.04,
                verified=True
            )
        ]
