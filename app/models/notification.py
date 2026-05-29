from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean

from app.database import Base


class Notification(Base):

    __tablename__ = 'notifications'

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    message = Column(String)

    type = Column(String)

    is_read = Column(
        Boolean,
        default=False
    )