from typing import List
from datetime import datetime
from app.sources.base import BaseSourceAdapter
from app.domain.signals import DemandSignal

class SearchSourceAdapter(BaseSourceAdapter):
    def __init__(self):
        super().__init__(source_name="search")

    async def fetch_signals(self) -> List[DemandSignal]:
        return [
            DemandSignal(
                source=self.source_name,
                source_id="search_501",
                raw_text="where to buy MacBook Pro M4 16-inch under $2500 in Germany",
                author_reference="anon_searcher",
                country="DE",
                timestamp=datetime.utcnow()
            )
        ]
