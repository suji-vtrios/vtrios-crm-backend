from pydantic import BaseModel


class MessageBase(
    BaseModel
):

    recipient: str

    content: str

    status: str

    channel: str


class Message(
    MessageBase
):

    id: int

    class Config:

        from_attributes = True