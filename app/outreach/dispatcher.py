import uuid
from datetime import datetime
from app.domain.offers import Offer
from app.domain.contacts import Contact, OutreachMessage
from app.config.settings import settings

class TwoMessageOutreachDispatcher:
    @staticmethod
    def create_permission_request(intent_id: str, contact: Contact, offer: Offer) -> OutreachMessage:
        body = (
            f"Hi! I noticed you are looking for {offer.title}. "
            f"I found a verified deal for around ${offer.price:.2f}. "
            f"Would you like me to send you the direct link?"
        )
        return OutreachMessage(
            message_id=f"msg_perm_{uuid.uuid4().hex[:8]}",
            intent_id=intent_id,
            contact_id=contact.contact_id or "temp_contact",
            message_type="PERMISSION_REQUEST",
            body=body,
            sent_at=datetime.utcnow()
        )

    @staticmethod
    def create_commercial_offer(intent_id: str, contact: Contact, offer: Offer) -> OutreachMessage:
        body = (
            f"Sure! Here is the link: {offer.affiliate_url}\n\n"
            f"{settings.AFFILIATE_DISCLOSURE_TEXT}"
        )
        return OutreachMessage(
            message_id=f"msg_comm_{uuid.uuid4().hex[:8]}",
            intent_id=intent_id,
            contact_id=contact.contact_id or "temp_contact",
            message_type="COMMERCIAL_OFFER",
            body=body,
            sent_at=datetime.utcnow()
        )
