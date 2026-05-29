from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class Course(Base):

    __tablename__ = 'courses'

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    duration = Column(String)

    fee = Column(String)