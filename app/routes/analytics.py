from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.lead import (
    Lead
)

router = APIRouter()


@router.get("/dashboard")
def get_dashboard_data(
    db: Session = Depends(get_db)
):

    leads = db.query(
        Lead
    ).all()

    total_leads = len(leads)

    converted_leads = len([

            lead

            for lead in leads

            if lead.status
            == 'Converted'
        ])

    interested_leads = len([

            lead

            for lead in leads

            if lead.status
            == 'Interested'
        ])

    followup_leads = len([

            lead

            for lead in leads

            if lead.status
            == 'Follow-up'
        ])

    counselor_stats = {}

    for lead in leads:

        counselor = lead.assigned_counselor

        if not counselor:

            continue

        if counselor not in counselor_stats:

            counselor_stats[
                counselor
            ] = {

                'total': 0,

                'converted': 0
            }

        counselor_stats[
            counselor
        ]['total'] += 1

        if lead.status == 'Converted':

            counselor_stats[
                counselor
            ]['converted'] += 1

    return {

        'total_leads':
            total_leads,

        'converted_leads':
            converted_leads,

        'interested_leads':
            interested_leads,

        'followup_leads':
            followup_leads,

        'counselor_stats':
            counselor_stats
    }