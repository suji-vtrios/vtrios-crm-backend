from fastapi import APIRouter
from app.config import settings

router = APIRouter()

@router.get("/webhook")
def verify_webhook(
    hub_mode: str = None,
    hub_verify_token: str = None,
    hub_challenge: str = None
):

    print(hub_mode)
    print(hub_verify_token)
    print(hub_challenge)

    if hub_verify_token == settings.META_VERIFY_TOKEN:
        return int(hub_challenge)

    return {"error": "Invalid token"}

@router.post("/webhook")
async def receive_lead(payload: dict):

    print("=" * 50)
    print(payload)
    print("=" * 50)

    return {
        "status": "received",
        "payload": payload
    }