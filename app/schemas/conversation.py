from pydantic import BaseModel


class ConversationBase(
    BaseModel
):

    lead_name: str

    platform: str

    last_message: str

    assigned_counselor: str

    status: str

    unread: bool = True


class Conversation(
    ConversationBase
):

    id: int

    class Config:

        from_attributes = True