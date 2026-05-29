from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base



class Lead(Base):

    __tablename__ = "leads"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    phone = Column(String)

    email = Column(String)

    course = Column(String)

    status = Column(String)

    next_followup = Column(String)
    assigned_counselor = Column(String)
    source = Column(String, default="Manual")

    platform = Column(String)

    campaign_name = Column(String)

    adset_name = Column(String)

    ad_name = Column(String)

    meta_lead_id = Column(String, unique=True)
    remarks = Column(String)

    lead_score = Column(Integer, default=0)

    utm_source = Column(String)

    utm_campaign = Column(String)

    utm_medium = Column(String)