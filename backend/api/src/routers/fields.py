from fastapi import APIRouter
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
    print("=============================================")
    print(field)
    print("=============================================")
    return field
