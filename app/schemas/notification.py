from pydantic import BaseModel


class NotificationBase(
    BaseModel
):

    message: str

    type: str

    is_read: bool = False


class Notification(
    NotificationBase
):

    id: int

    class Config:

        from_attributes = True