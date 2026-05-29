from pydantic import BaseModel

class LeadBase(BaseModel):

    name: str

    phone: str

    email: str

    course: str

    source: str

    status: str

    next_followup: str | None = None

    assigned_counselor: str | None = None

class LeadCreate(
    LeadBase
):
    pass

class Lead(
    LeadBase
):

    id: int

    followup_status: str | None = None

    lead_score: int | None = None

    lead_temperature: str | None = None