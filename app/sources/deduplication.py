import hashlib
from typing import Optional
from sqlalchemy.orm import Session
from app.domain.signals import DemandSignal
from app.database.models import DBDemandSignal

class DeduplicationService:
    @staticmethod
    def generate_fingerprint(text: str, author_ref: Optional[str] = None) -> str:
        clean_text = "".join(text.lower().split())
        data = f"{author_ref or ''}:{clean_text}"
        return hashlib.sha256(data.encode("utf-8")).hexdigest()

    @classmethod
    def is_duplicate(cls, db: Session, signal: DemandSignal) -> bool:
        fingerprint = cls.generate_fingerprint(signal.raw_text, signal.author_reference)
        signal.fingerprint = fingerprint

        existing = db.query(DBDemandSignal).filter(
            DBDemandSignal.fingerprint == fingerprint
        ).first()

        return existing is not None
