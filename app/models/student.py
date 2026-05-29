from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class Student(Base):

    __tablename__ = "students"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    phone = Column(String)

    email = Column(String)

    course = Column(String)

    enrollment_date = Column(String)

    status = Column(String)