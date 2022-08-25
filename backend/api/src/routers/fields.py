from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from api.src.database import get_db
from api.src.repositories import RepoFields
from api.src.routers.common.schemas import FieldPost, FieldResponse

router = APIRouter()


@router.post('/fields', tags=['Fields'], response_model=FieldResponse)
def add_field(data: FieldPost, db: Session = Depends(get_db)):
    repo = RepoFields(db)
    field = repo.create_field(**data.dict())
    return field


@router.get('/fields', tags=['Fields'], response_model=list[FieldResponse])
def get_fields(db: Session = Depends(get_db)):
    repo = RepoFields(db)
    fields = repo.get_fields()
    return fields


@router.get('/fields/{field_id}', tags=['Fields'], response_model=FieldResponse)
def get_field(field_id, db: Session = Depends(get_db)):
    repo = RepoFields(db)
    field = repo.get_field_by_id(field_id)
    if field:
        return field
    else:
        raise HTTPException(404, "Field not found")
