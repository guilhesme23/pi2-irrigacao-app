from fastapi import APIRouter

router = APIRouter()

@router.get("/sensors/")
def get_sensors_data():
	return {"message": "Sensors data"}

