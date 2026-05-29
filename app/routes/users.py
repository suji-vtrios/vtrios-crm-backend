from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.user import (
    User as UserModel
)

from app.schemas.user import (
    User
)

from app.security import (
    hash_password
)

router = APIRouter()


@router.get("/")
def get_users(
    db: Session = Depends(get_db)
):

    return db.query(
        UserModel
    ).all()


@router.post("/")
def create_user(
    user: User,
    db: Session = Depends(get_db)
):

    existing_user = db.query(
        UserModel
    ).filter(
        UserModel.email
        == user.email
    ).first()

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail=
            "Email already exists"
        )

    new_user = UserModel(

        name=user.name,

        email=user.email,

        password=
        hash_password(
            user.password
        ),

        role=user.role,

        status=user.status
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return new_user


@router.put("/{id}")
def update_user(
    id: int,
    user: User,
    db: Session = Depends(get_db)
):

    existing_user = db.query(
        UserModel
    ).filter(
        UserModel.id
        == id
    ).first()

    if not existing_user:

        raise HTTPException(
            status_code=404,
            detail=
            "User not found"
        )

    existing_user.name = user.name
    existing_user.email = user.email
    existing_user.role = user.role
    existing_user.status = user.status

    db.commit()

    db.refresh(
        existing_user
    )

    return existing_user


@router.delete("/{id}")
def delete_user(
    id: int,
    db: Session = Depends(get_db)
):

    user = db.query(
        UserModel
    ).filter(
        UserModel.id
        == id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail=
            "User not found"
        )

    db.delete(user)

    db.commit()

    return {
        "message":
        "User deleted"
    }