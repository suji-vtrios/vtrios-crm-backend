from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.counselor import (
    Counselor as CounselorModel
)

from app.schemas.counselor import (
    Counselor
)

router = APIRouter()


@router.get("/")
def get_counselors(
    db: Session = Depends(get_db)
):

    return db.query(
        CounselorModel
    ).all()


@router.post("/")
def create_counselor(
    counselor: Counselor,
    db: Session = Depends(get_db)
):

    item = CounselorModel(

        name=counselor.name,

        phone=counselor.phone,

        email=counselor.email,

        role=counselor.role,

        status=counselor.status,

        branch=counselor.branch
    )

    db.add(item)

    db.commit()

    db.refresh(item)

    return item


@router.put("/{counselor_id}")
def update_counselor(
    counselor_id: int,
    counselor: Counselor,
    db: Session = Depends(get_db)
):

    item = db.query(
        CounselorModel
    ).filter(
        CounselorModel.id
        == counselor_id
    ).first()

    if not item:
        return {
            "message":
            "Counselor not found"
        }

    item.name = counselor.name

    item.phone = counselor.phone

    item.email = counselor.email

    item.role = counselor.role

    item.status = counselor.status

    item.branch = counselor.branch

    db.commit()

    db.refresh(item)

    return item