from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class Counselor(Base):

    __tablename__ = "counselors"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    name = Column(String)

    phone = Column(String)

    email = Column(String)

    role = Column(String)

    status = Column(String)

    branch = Column(String)