from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class Message(Base):

    __tablename__ = 'messages'

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    recipient = Column(String)

    content = Column(String)

    status = Column(String)

    channel = Column(String)