from fastapi import APIRouter
from fastapi import Request

from app.database import SessionLocal

from app.models.conversation import (
    Conversation
)

from app.models.notification import (
    Notification
)
from app.config import settings

router = APIRouter()


VERIFY_TOKEN = settings.META_VERIFY_TOKEN


@router.get("/meta")
async def verify_webhook(
    request: Request
):

    params = request.query_params

    mode = params.get(
            "hub.mode"
        )

    token = params.get(
            "hub.verify_token"
        )

    challenge = params.get(
            "hub.challenge"
        )

    if (

        mode == "subscribe"

        and

        token == VERIFY_TOKEN
    ):

        return int(challenge)

    return {
        "error":
        "Verification failed"
    }


@router.post("/meta")
async def receive_webhook(
    request: Request
):

    payload = await request.json()

    db = SessionLocal()

    try:

        entry_list = payload.get(
                "entry",
                []
            )

        for entry in entry_list:

            messaging = entry.get(
                    "messaging",
                    []
                )

            for message_event in messaging: 
                sender_id = message_event[
                            "sender"
                        ]["id"]
                message_text = message_event.get(
                            "message",
                            {}
                        ).get(
                            "text",
                            ""
                        ) 
                new_conversation = Conversation(

                        lead_name=
                        sender_id,

                        platform=
                        "Instagram",

                        last_message=
                        message_text,

                        assigned_counselor=
                        "Unassigned",

                        status=
                        "Open",

                        unread=True
                    ) 
                db.add(
                    new_conversation
                ) 
                notification = Notification(

                        message=(

                            "📸 New Instagram "

                            "message received"
                        ),

                        type="Conversation"
                    ) 
                db.add(
                    notification
                )

        db.commit()

    finally:

        db.close()

    return {
        "status":
        "received"
    }