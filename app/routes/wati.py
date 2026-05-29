from fastapi import APIRouter
from app.config import settings
from app.services.wati_service import send_welcome_message
import requests

router = APIRouter()


@router.post("/test")
def test_wati():

    return send_welcome_message(
        "918891393010",
        "Suji"
    )


@router.get("/channels")
def get_channels():

    response = requests.get(
        f"{settings.WATI_API_URL}/api/ext/v3/channels?page_number=1&page_size=10",
        headers={
            "Authorization": f"Bearer {settings.WATI_API_KEY}"
        }
    )

    return response.json()


@router.get("/templates")
def get_templates():

    response = requests.get(
        f"{settings.WATI_API_URL}/api/ext/v3/messageTemplates?page_number=1&page_size=100",
        headers={
            "Authorization": f"Bearer {settings.WATI_API_KEY}"
        }
    )

    print("STATUS =", response.status_code)
    print("TEXT =", response.text)

    return {
        "status": response.status_code,
        "response": response.text
    }

@router.get("/templates-raw")
def get_templates_raw():

    response = requests.get(
        f"{settings.WATI_API_URL}/api/ext/v3/messageTemplates",
        headers={
            "Authorization": f"Bearer {settings.WATI_API_KEY}"
        }
    )

    return {
        "status": response.status_code,
        "response": response.text
    }

@router.get("/contacts")
def contacts():

    response = requests.get(
        f"{settings.WATI_API_URL}/api/ext/v3/contacts?page_number=1&page_size=10",
        headers={
            "Authorization": f"Bearer {settings.WATI_API_KEY}"
        }
    )

    return {
        "status": response.status_code,
        "response": response.text
    }