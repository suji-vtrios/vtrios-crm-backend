from pydantic import BaseModel


class FollowUp(BaseModel):

    id: int

    lead_id: int

    followup_date: str

    remarks: str

    status: str

    next_followup: str