from pydantic import BaseModel


class Batch(BaseModel):

    id: int | None = None

    name: str

    course: str

    trainer: str

    start_date: str

    end_date: str

    timing: str

    mode: str

    status: str