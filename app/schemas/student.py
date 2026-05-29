from pydantic import BaseModel


class Student(BaseModel):

    id: int

    name: str

    phone: str

    email: str

    course: str

    enrollment_date: str

    status: str