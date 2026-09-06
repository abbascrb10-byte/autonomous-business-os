from datetime import datetime
from sqlalchemy.orm import Session
from app.database.models import DBAnalyticsEvent

class ConversionTracker:
    @staticmethod
    def record_conversion(db: Session, offer_id: str, amount: float) -> DBAnalyticsEvent:
        event = DBAnalyticsEvent(
            event_type="CONVERSION",
            entity_id=offer_id,
            event_data={"amount": amount},
            timestamp=datetime.utcnow()
        )
        db.add(event)
        db.commit()
        db.refresh(event)
        return event
