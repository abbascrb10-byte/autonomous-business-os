import uuid
from typing import List
from app.merchants.base import BaseMerchantAdapter
from app.domain.offers import Offer
from app.domain.intents import ExtractedProductRequirements

class EBayAdapter(BaseMerchantAdapter):
    def __init__(self):
        super().__init__(merchant_name="eBay")

    async def search_offers(self, requirements: ExtractedProductRequirements) -> List[Offer]:
        product_name = requirements.product_name or "Item"
        price = requirements.budget or 199.99
        product_id = f"prod_ebay_{uuid.uuid4().hex[:8]}"

        affiliate_url = f"https://www.ebay.com/itm/123456789?mkevt=1&mkcid=1&mkrid=711-53200-19255-0"

        return [
            Offer(
                offer_id=f"off_ebay_{uuid.uuid4().hex[:8]}",
                product_id=product_id,
                merchant=self.merchant_name,
                title=f"{product_name} - Trusted eBay Top Seller",
                price=round(price * 0.90, 2),
                currency=requirements.currency or "USD",
                in_stock=True,
                seller="TopRatedSeller",
                shipping_destination=requirements.destination_country or "US",
                shipping_cost=5.00,
                rating=4.8,
                affiliate_url=affiliate_url,
                commission_rate=0.05,
                verified=True
            )
        ]
