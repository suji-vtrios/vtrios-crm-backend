from fastapi import APIRouter
from fastapi import Depends
from datetime import datetime
from datetime import timedelta

from sqlalchemy.orm import Session

from app.schemas.lead import Lead
from app.schemas.lead import LeadCreate
from app.models.lead import Lead as LeadModel

from app.dependencies import get_db
from app.models.notification import ( Notification )

router = APIRouter()

@router.get("/")
def get_leads(
    db: Session = Depends(get_db)
):

    leads = db.query(
        LeadModel
    ).all()

    today = datetime.now().date()

    result = []

    for lead in leads:

        followup_status = None

        if lead.next_followup:

            followup_date = (
                datetime.strptime(
                    lead.next_followup,
                    '%Y-%m-%d'
                ).date()
            )

            if followup_date < today:

                followup_status = (
                    'Overdue'
                )

            elif followup_date == today:

                followup_status = (
                    'Today'
                )

            else:

                followup_status = (
                    'Upcoming'
                )

        score = 0

        if lead.status == 'New':

            score = 10

        elif lead.status == 'Interested':

            score = 30

        elif lead.status == 'Follow-up':

            score = 50

        elif lead.status == 'Converted':

            score = 100

        if followup_status == 'Overdue':

            score -= 10

        if score >= 80:

            temperature = 'Hot'

        elif score >= 40:

            temperature = 'Warm'

        else:

            temperature = 'Cold'

        result.append({

            "id": lead.id,

            "name": lead.name,

            "phone": lead.phone,

            "email": lead.email,

            "course": lead.course,

            "source": lead.source,

            "status": lead.status,

            "next_followup":
                lead.next_followup,

            "assigned_counselor":
                lead.assigned_counselor,

            "followup_status":
                followup_status,

            "lead_score":
                score,

            "lead_temperature":
                temperature
        })

    return result


@router.post("/")
def create_lead(
    lead: LeadCreate,
    db: Session = Depends(get_db)
):

    from app.models.counselor import (
        Counselor
    )
    counselors = db.query(
        Counselor
    ).all()

    assigned_counselor = None

    if counselors:

        latest_lead = db.query(
            LeadModel
        ).order_by(
            LeadModel.id.desc()
        ).first()

        if latest_lead:

            last_index = next(

                (
                    index

                    for index,
                    counselor

                    in enumerate(
                        counselors
                    )

                    if counselor.name
                    == latest_lead
                    .assigned_counselor
                ),

                -1
            )

            next_index = (
                last_index + 1
            ) % len(counselors)

        else:

            next_index = 0

        assigned_counselor = (
            counselors[
                next_index
            ].name
        )

    next_followup = (
        datetime.now()
        + timedelta(days=1)
    ).strftime('%Y-%m-%d')
    
    new_lead = LeadModel(
        name=lead.name,
        phone=lead.phone,
        email=lead.email,
        course=lead.course,
        source=lead.source,
        status=lead.status,
        next_followup= next_followup,
        assigned_counselor = assigned_counselor
    )

    db.add(new_lead)

    db.commit()
    notification = Notification(

        message = (

            f"📞 New lead "

            f"{new_lead.name} "

            f"assigned to "

            f"{assigned_counselor}"
        ),

        type = "Lead"
    )

    db.add(notification)

    db.commit()

    db.refresh(new_lead)

    return {
        "message": "Lead created",
        "lead": new_lead
    }

@router.get("/{lead_id}")
def get_lead(
    lead_id: int,
    db: Session = Depends(get_db)
):
    return db.query(
        LeadModel
    ).filter(
        LeadModel.id == lead_id
    ).first()

@router.put("/{lead_id}")
def update_lead(
    lead_id: int,
    lead: LeadCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(
        LeadModel
    ).filter(
        LeadModel.id == lead_id
    ).first()

    if not existing:
        return {
            "message": "Lead not found"
        }

    existing.name = lead.name
    existing.phone = lead.phone
    existing.email = lead.email
    existing.course = lead.course
    existing.source = lead.source
    existing.status = lead.status

    db.commit()

    return {
        "message": "Lead updated"
    }

@router.delete("/{lead_id}")
def delete_lead(
    lead_id: int,
    db: Session = Depends(get_db)
):

    existing = db.query(
        LeadModel
    ).filter(
        LeadModel.id == lead_id
    ).first()

    if not existing:
        return {
            "message": "Lead not found"
        }

    db.delete(existing)

    db.commit()

    return {
        "message": "Lead deleted"
    }