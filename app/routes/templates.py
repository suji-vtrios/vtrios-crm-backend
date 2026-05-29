from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.template import (
    Template as TemplateModel
)

from app.schemas.template import (
    TemplateBase
)

router = APIRouter()


@router.get("/")
def get_templates(
    db: Session = Depends(get_db)
):

    return db.query(
        TemplateModel
    ).all()


@router.post("/")
def create_template(
    template: TemplateBase,
    db: Session = Depends(get_db)
):

    new_template = TemplateModel(

        name=
        template.name,

        channel=
        template.channel,

        content=
        template.content
    )

    db.add(
        new_template
    )

    db.commit()

    db.refresh(
        new_template
    )

    return new_template


@router.put("/{id}")
def update_template(
    id: int,
    template: TemplateBase,
    db: Session = Depends(get_db)
):

    existing_template = db.query(
        TemplateModel
    ).filter(
        TemplateModel.id
        == id
    ).first()

    if not existing_template:

        raise HTTPException(
            status_code=404,
            detail=
            "Template not found"
        )

    existing_template.name = template.name

    existing_template.channel = template.channel

    existing_template.content = template.content

    db.commit()

    db.refresh(
        existing_template
    )

    return existing_template


@router.delete("/{id}")
def delete_template(
    id: int,
    db: Session = Depends(get_db)
):

    template = db.query(
        TemplateModel
    ).filter(
        TemplateModel.id
        == id
    ).first()

    if not template:

        raise HTTPException(
            status_code=404,
            detail=
            "Template not found"
        )

    db.delete(template)

    db.commit()

    return {

        "message":
        "Template deleted"
    }