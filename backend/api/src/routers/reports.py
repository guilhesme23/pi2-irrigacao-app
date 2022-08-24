from datetime import datetime
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from pydantic import BaseModel
from api.src.models import reports_enum
from api.src.database import get_db
from sqlalchemy.orm import Session
from api.src.repositories import RepoReports


router = APIRouter()


class AddReport(BaseModel):
    battery_level: float
    remaining_points: dict
    status_report: reports_enum


class ReportResponse(BaseModel):
    id: int
    battery_level: float
    remaining_points: dict
    status_report: reports_enum
    recorded_on: datetime

    class Config:
        orm_mode = True


@router.post(
    '/reports',
    tags=['Reports'],
    response_model=ReportResponse,
    description="Create a report of the robot status"
)
def add_report(data: AddReport, db: Session = Depends(get_db)):
    print(data)
    try:
        repo = RepoReports(db)
        report = repo.create_report(**data.dict())
        return report
    except:
        raise HTTPException(400, "Error creating report")
