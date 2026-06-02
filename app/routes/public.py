from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from datetime import datetime
from datetime import timedelta

from app.dependencies import get_db

from app.models.lead import (
    Lead as LeadModel
)

from app.models.user import (
    User
)

from app.schemas.lead import (
    LeadCreate
)
from app.models.notification import (
    Notification
)

router = APIRouter()


@router.post("/leads")
def create_public_lead(
    lead: LeadCreate,
    db: Session = Depends(get_db)
):

    counselors = db.query(
        User
    ).filter(
        User.role == "Counselor"
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

        status='New',

        next_followup=
            next_followup,

        assigned_counselor=
            assigned_counselor
    )

    db.add(new_lead)

    db.commit()
    notification = Notification(

        message = (

            f"🌐 Public lead "

            f"{new_lead.name} "

            f"received from "

            f"{new_lead.source}"
        ),

        type = "Lead"
    )

    db.add(notification)

    db.commit()

    db.refresh(new_lead)

    return {

        "message":
            "Lead created successfully",

        "assigned_counselor":
            assigned_counselor
    }