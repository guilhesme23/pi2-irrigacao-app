from fastapi import APIRouter
from pydantic import BaseModel
from api.src.database import get_db
from fastapi.params import Depends
from api.src.repositories import RepoIrrigation
from sqlalchemy.orm import Session

from api.src.models import irrigation_enum

router = APIRouter()


class SetIrrigateState(BaseModel):
    irrigate: bool


@router.get("/commands/irrigate", tags=["Commands"])
def get_start(db: Session = Depends(get_db)):
    irrigate = False
    repo = RepoIrrigation(db)
    state = repo.get_current_irrigation_state()
    message = "Stop irrigation"
    if state == irrigation_enum.START:
        irrigate = True
    if irrigate:
        message = "Start irrigation"
    return {"message": message, "data": irrigate}


@router.post("/commands/irrigate", tags=["Commands"])
def post_start(data: SetIrrigateState, db: Session = Depends(get_db)):
    irrigate = data.irrigate
    repo = RepoIrrigation(db)
    state = irrigation_enum.START
    if not irrigate:
        state = irrigation_enum.STOP
    repo.set_irrigation_state(state)
    message = "Stop irrigation"
    if irrigate:
        message = "Start irrigation"
    return {"message": message}
