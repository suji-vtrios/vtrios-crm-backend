import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    DATABASE_URL = os.getenv(
        "DATABASE_URL"
    )

    JWT_SECRET = os.getenv(
        "JWT_SECRET"
    )

    META_VERIFY_TOKEN = os.getenv(
        "META_VERIFY_TOKEN"
    )

    WATI_API_KEY = os.getenv(
        "WATI_API_KEY"
    )

    WATI_API_URL = os.getenv(
        "WATI_API_URL"
    )

    WATI_CHANNEL_ID = os.getenv(
        "WATI_CHANNEL_ID"
    )

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY"
    )

    FRONTEND_URL = os.getenv(
        "FRONTEND_URL"
    )


settings = Settings()