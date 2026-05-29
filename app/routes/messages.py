from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.message import (
    Message as MessageModel
)

from app.schemas.message import (
    MessageBase
)

router = APIRouter()


@router.get("/")
def get_messages(
    db: Session = Depends(get_db)
):

    return db.query(
        MessageModel
    ).order_by(
        MessageModel.id.desc()
    ).all()


@router.post("/send")
def send_message(
    message: MessageBase,
    db: Session = Depends(get_db)
):

    new_message = MessageModel(

        recipient=
        message.recipient,

        content=
        message.content,

        status='Sent',

        channel=
        message.channel
    )

    db.add(new_message)

    db.commit()

    db.refresh(new_message)

    return {

        "message":
        "Message processed",

        "data":
        new_message
    }