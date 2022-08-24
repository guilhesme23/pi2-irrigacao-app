from fastapi import APIRouter
from pydantic import BaseModel
from api.src.database import get_db
from fastapi.params import Depends
from api.src.repositories import RepoIrrigation
from sqlalchemy.orm import Session

from api.src.models import irrigation_enum

router = APIRouter()

irrigate = False


class SetIrrigateState(BaseModel):
    irrigate: bool


@router.get("/bot", tags=["Bot"])
def get_start():
    message = "Stop irrigation"
    if irrigate:
        message = "Start irrigation"
    return {"message": message, "data": irrigate}


@router.post("/bot", tags=["Bot"])
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
