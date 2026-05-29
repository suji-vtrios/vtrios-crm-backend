from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    name = Column(String)

    email = Column(
        String,
        unique=True
    )

    password = Column(String)

    role = Column(String)

    status = Column(String)