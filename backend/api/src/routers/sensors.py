from fastapi import Body, APIRouter

router = APIRouter()

@router.get("/sensors")
def get_sensors_data():
	return {"message": "Sensors data"}

@router.post("/sensors")
def add_sensor_data(data = Body()):
	print(data)
	return data
