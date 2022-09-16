from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from api.src.database import get_db
from api.src.repositories import RepoFields
from api.src.routers.common.schemas import FieldPost, FieldResponse
from mapping.core.networkx_grid_route import gen_grid
import networkx as nx

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
        grid = gen_grid(field.field_width, field.field_length, [])
        grid = nx.to_dict_of_lists(grid)
        return {
            'id': field.id,
            'field_width': field.field_width,
            'field_length': field.field_length,
            'grid': list(grid.keys()),
            'radius': 3
        }
    else:
        raise HTTPException(404, "Field not found")
