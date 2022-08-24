from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.params import Depends
from api.src.database import get_db
from api.src.repositories import RepoSensors

router = APIRouter()

class SensorRecordPost(BaseModel):
	temp_air: float
	temp_soil: float
	humidity_air: float
	humidity_soil: float

class SensorData(BaseModel):
	temp_air: float
	temp_soil: float
	humidity_air: float
	humidity_soil: float
	recorded_on: datetime

	class Config:
		orm_mode = True

@router.get("/sensors", tags = ["Sensors"])
def get_sensors_data():
	return {"message": "Sensors data"}

@router.post("/sensors", tags = ["Sensors"], response_model=SensorData)
def add_sensor_data(data: SensorRecordPost, db: Session = Depends(get_db)):
	repo = RepoSensors(db)
	sensors_data = repo.record_sensor_data(
		data.temp_air,
		data.temp_soil,
		data.humidity_air,
		data.humidity_soil
	)
	return sensors_data
