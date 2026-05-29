from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database import Base


class FollowUp(Base):

    __tablename__ = "followups"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    lead_id = Column(
        Integer,
        ForeignKey("leads.id")
    )

    followup_date = Column(String)

    remarks = Column(String)

    status = Column(String)

    next_followup = Column(String)