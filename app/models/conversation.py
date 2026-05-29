from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean

from app.database import Base


class Conversation(Base):

    __tablename__ = 'conversations'

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    lead_name = Column(String)

    platform = Column(String)

    last_message = Column(String)

    assigned_counselor = Column(String)

    status = Column(String)

    unread = Column(
        Boolean,
        default=True
    )