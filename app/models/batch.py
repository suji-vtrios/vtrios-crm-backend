from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class Batch(Base):

    __tablename__ = "batches"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    name = Column(String)

    course = Column(String)

    trainer = Column(String)

    start_date = Column(String)

    end_date = Column(String)

    timing = Column(String)

    mode = Column(String)

    status = Column(String)