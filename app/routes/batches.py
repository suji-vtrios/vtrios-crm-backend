from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.batch import (
    Batch as BatchModel
)

from app.schemas.batch import (
    Batch
)

router = APIRouter()


@router.get("/")
def get_batches(
    db: Session = Depends(get_db)
):

    return db.query(
        BatchModel
    ).all()


@router.post("/")
def create_batch(
    batch: Batch,
    db: Session = Depends(get_db)
):

    item = BatchModel(
        id=batch.id,
        name=batch.name,
        course=batch.course,
        trainer=batch.trainer,
        start_date=batch.start_date,
        end_date=batch.end_date,
        timing=batch.timing,
        mode=batch.mode,
        status=batch.status
    )

    db.add(item)

    db.commit()

    db.refresh(item)

    return item

@router.put("/{batch_id}")
def update_batch(
    batch_id: int,
    batch: Batch,
    db: Session = Depends(get_db)
):

    item = db.query(
        BatchModel
    ).filter(
        BatchModel.id == batch_id
    ).first()

    if not item:
        return {
            "message": "Batch not found"
        }

    item.name = batch.name
    item.course = batch.course
    item.trainer = batch.trainer
    item.start_date = batch.start_date
    item.end_date = batch.end_date
    item.timing = batch.timing
    item.mode = batch.mode
    item.status = batch.status

    db.commit()

    db.refresh(item)

    return item