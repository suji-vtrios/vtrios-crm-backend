from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.followup import (
    FollowUp as FollowUpModel
)

from app.models.lead import (
    Lead as LeadModel
)

from app.schemas.followup import (
    FollowUp
)

router = APIRouter()


@router.get("/")
def get_followups(
    db: Session = Depends(get_db)
):
    return db.query(
        FollowUpModel
    ).all()


@router.get("/lead/{lead_id}")
def get_lead_followups(
    lead_id: int,
    db: Session = Depends(get_db)
):
    return db.query(
        FollowUpModel
    ).filter(
        FollowUpModel.lead_id
        == lead_id
    ).all()


@router.post("/")
def create_followup(
    followup: FollowUp,
    db: Session = Depends(get_db)
):

    item = FollowUpModel(
        id=followup.id,
        lead_id=followup.lead_id,
        followup_date=
        followup.followup_date,
        remarks=
        followup.remarks,
        status=
        followup.status,
        next_followup=
        followup.next_followup
    )

    db.add(item)

    # Update Lead Next Follow-up
    lead = db.query(
        LeadModel
    ).filter(
        LeadModel.id ==
        followup.lead_id
    ).first()

    if lead:
        lead.next_followup = (
            followup.next_followup
        )

    db.commit()

    db.refresh(item)

    return item


@router.delete("/{id}")
def delete_followup(
    id: int,
    db: Session = Depends(get_db)
):

    item = db.query(
        FollowUpModel
    ).filter(
        FollowUpModel.id == id
    ).first()

    if not item:
        return {
            "message":
            "Follow-up not found"
        }

    db.delete(item)

    db.commit()

    return {
        "message":
        "Follow-up deleted"
    }