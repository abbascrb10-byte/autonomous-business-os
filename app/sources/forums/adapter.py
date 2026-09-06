from typing import List
from datetime import datetime
from app.sources.base import BaseSourceAdapter
from app.domain.signals import DemandSignal

class ForumsSourceAdapter(BaseSourceAdapter):
    def __init__(self):
        super().__init__(source_name="forums")

    async def fetch_signals(self) -> List[DemandSignal]:
        return [
            DemandSignal(
                source=self.source_name,
                source_id="forum_302",
                raw_text="Looking for recommendation on noise cancelling headphones under $300.",
                author_reference="forum_member_99",
                country="US",
                timestamp=datetime.utcnow()
            )
        ]
