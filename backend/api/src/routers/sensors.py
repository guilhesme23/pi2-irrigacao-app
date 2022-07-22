from fastapi import Body, APIRouter

router = APIRouter()

@router.get("/sensors", tags = ["Sensors"])
def get_sensors_data():
	return {"message": "Sensors data"}

@router.post("/sensors", tags = ["Sensors"])
def add_sensor_data(data = Body()):
	print(data)
	return data
