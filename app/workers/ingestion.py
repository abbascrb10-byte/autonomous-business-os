import asyncio
from app.sources.requests.adapter import RequestsSourceAdapter
from app.sources.deduplication import DeduplicationService
from app.database.session import SessionLocal
from app.database.models import DBDemandSignal

async def run_ingestion_worker():
    db = SessionLocal()
    adapter = RequestsSourceAdapter()
    signals = await adapter.fetch_signals()

    saved_count = 0
    for sig in signals:
        if not DeduplicationService.is_duplicate(db, sig):
            db_sig = DBDemandSignal(
                source=sig.source,
                source_id=sig.source_id,
                raw_text=sig.raw_text,
                author_reference=sig.author_reference,
                country=sig.country,
                fingerprint=sig.fingerprint
            )
            db.add(db_sig)
            saved_count += 1

    db.commit()
    db.close()
    return saved_count
