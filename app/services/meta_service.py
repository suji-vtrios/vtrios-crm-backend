from app.database import SessionLocal
from app.models.lead import Lead


def create_meta_lead(data):

    db = SessionLocal()

    lead = Lead(
        name=data.get("name"),
        email=data.get("email"),
        phone=data.get("phone"),

        source="Meta",

        platform=data.get("platform"),

        campaign_name=data.get("campaign_name"),

        adset_name=data.get("adset_name"),

        ad_name=data.get("ad_name"),

        meta_lead_id=data.get("meta_lead_id")
    )

    db.add(lead)

    db.commit()

    db.refresh(lead)

    return lead