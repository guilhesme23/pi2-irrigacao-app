from fastapi import APIRouter

router = APIRouter()

@router.get("/trajectory/")
def get_sensors_data():
	return {"message": "trajectory data"}

