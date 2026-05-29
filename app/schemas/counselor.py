from pydantic import BaseModel


class Counselor(BaseModel):

    id: int | None = None

    name: str

    phone: str

    email: str

    role: str

    status: str

    branch: str