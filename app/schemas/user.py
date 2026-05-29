from pydantic import BaseModel


class User(BaseModel):

    id: int | None = None

    name: str

    email: str

    password: str

    role: str

    status: str


class LoginRequest(
    BaseModel
):

    email: str

    password: str