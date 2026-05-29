from pydantic import BaseModel


class TemplateBase(
    BaseModel
):

    name: str

    channel: str

    content: str


class Template(
    TemplateBase
):

    id: int

    class Config:

        from_attributes = True