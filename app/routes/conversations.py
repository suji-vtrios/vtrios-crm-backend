from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.conversation import (
    Conversation as ConversationModel
)

from app.schemas.conversation import ( ConversationBase )

router = APIRouter()


@router.get("/")
def get_conversations(
    db: Session = Depends(get_db)
):

    return db.query(
        ConversationModel
    ).order_by(
        ConversationModel.id.desc()
    ).all()


@router.post("/")
def create_conversation(
    conversation: ConversationBase,
    db: Session = Depends(get_db)
):

    new_conversation = ConversationModel(

        lead_name=
        conversation.lead_name,

        platform=
        conversation.platform,

        last_message=
        conversation.last_message,

        assigned_counselor=
        conversation.assigned_counselor,

        status=
        conversation.status,

        unread=
        conversation.unread
    )

    db.add(
        new_conversation
    )

    db.commit()

    db.refresh(
        new_conversation
    )

    return new_conversation


@router.put("/{id}/read")
def mark_conversation_read(
    id: int,
    db: Session = Depends(get_db)
):

    conversation = db.query(
        ConversationModel
    ).filter(
        ConversationModel.id
        == id
    ).first()

    if not conversation:

        raise HTTPException(
            status_code=404,
            detail=
            "Conversation not found"
        )

    conversation.unread = False

    db.commit()

    db.refresh(
        conversation
    )

    return conversation