from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database import Base


class Template(Base):

    __tablename__ = 'templates'

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    channel = Column(String)

    content = Column(Text)