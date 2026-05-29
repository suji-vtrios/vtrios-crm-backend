from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.user import (
    User as UserModel
)

from app.schemas.user import (
    User,
    LoginRequest
)

from app.security import (
    hash_password,
    verify_password
)

router = APIRouter()


@router.post("/register")
def register_user(
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

    return {
        "message":
        "User created"
    }


@router.post("/login")
def login_user(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    user = db.query(
        UserModel
    ).filter(
        UserModel.email
        == request.email
    ).first()

    if not user:

        raise HTTPException(
            status_code=401,
            detail=
            "Invalid credentials"
        )

    if not verify_password(
        request.password,
        user.password
    ):

        raise HTTPException(
            status_code=401,
            detail=
            "Invalid credentials"
        )

    return {

        "id": user.id,

        "name": user.name,

        "email": user.email,

        "role": user.role
    }