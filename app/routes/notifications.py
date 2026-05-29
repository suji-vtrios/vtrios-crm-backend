from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.notification import (
    Notification as NotificationModel
)
from app.schemas.notification import (
    NotificationBase
)

router = APIRouter()


@router.get("/")
def get_notifications(
    db: Session = Depends(get_db)
):

    return db.query(
        NotificationModel
    ).order_by(
        NotificationModel.id.desc()
    ).all()


@router.post("/")
def create_notification(
    notification: NotificationBase,
    db: Session = Depends(get_db)
):

    new_notification = NotificationModel(

        message=
        notification.message,

        type=
        notification.type,

        is_read=
        notification.is_read
    )

    db.add(
        new_notification
    )

    db.commit()

    db.refresh(
        new_notification
    )

    return new_notification


@router.put("/{id}/read")
def mark_as_read(
    id: int,
    db: Session = Depends(get_db)
):

    notification = db.query(
        NotificationModel
    ).filter(
        NotificationModel.id
        == id
    ).first()

    if notification:

        notification.is_read = True

        db.commit()

    return {
        "message":
        "Notification updated"
    }