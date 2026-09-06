from datetime import datetime
from sqlalchemy.orm import Session
from app.database.models import DBAnalyticsEvent

class ClickTracker:
    @staticmethod
    def record_click(db: Session, offer_id: str, contact_id: str) -> DBAnalyticsEvent:
        event = DBAnalyticsEvent(
            event_type="CLICK",
            entity_id=offer_id,
            event_data={"contact_id": contact_id},
            timestamp=datetime.utcnow()
        )
        db.add(event)
        db.commit()
        db.refresh(event)
        return event
