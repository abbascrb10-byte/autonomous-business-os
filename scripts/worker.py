import asyncio
from app.workers import run_ingestion_worker, run_classification_worker

async def main():
    print("Running background worker cycle...")
    ingested = await run_ingestion_worker()
    classified = await run_classification_worker()
    print(f"Worker cycle finished: Ingested {ingested} signals, Classified {classified} intents.")

if __name__ == "__main__":
    asyncio.run(main())
