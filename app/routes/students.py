from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.student import (
    Student as StudentModel
)

from app.schemas.student import (
    Student
)

router = APIRouter()


@router.get("/")
def get_students(
    db: Session = Depends(get_db)
):

    return db.query(
        StudentModel
    ).all()


@router.post("/")
def create_student(
    student: Student,
    db: Session = Depends(get_db)
):

    item = StudentModel(
        id=student.id,
        name=student.name,
        phone=student.phone,
        email=student.email,
        course=student.course,
        enrollment_date=
        student.enrollment_date,
        status=student.status
    )

    db.add(item)

    db.commit()

    db.refresh(item)

    return item