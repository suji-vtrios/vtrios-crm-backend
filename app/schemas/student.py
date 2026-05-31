from pydantic import BaseModel


class StudentBase(BaseModel):

    name: str

    phone: str

    email: str

    course: str

    enrollment_date: str

    status: str


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):

    id: int