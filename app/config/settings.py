import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "GPIE - Global Purchase Intent Engine"
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"

    DATABASE_URL: str = "sqlite:///./gpie.db"
    REDIS_URL: str = "redis://localhost:6379/0"

    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    GEMINI_API_KEY: str = ""

    AMAZON_ASSOCIATES_TAG: str = ""
    AMAZON_CREATORS_API_KEY: str = ""
    EBAY_CLIENT_ID: str = ""
    EBAY_CLIENT_SECRET: str = ""

    BASE_URL: str = "http://localhost:8000"
    AFFILIATE_DISCLOSURE_TEXT: str = (
        "Disclosure: We may earn an affiliate commission at no extra cost to you if you purchase through our links."
    )

    class Config:
        env_file = ".env"

settings = Settings()
