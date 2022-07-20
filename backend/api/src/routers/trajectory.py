from fastapi import APIRouter
from mapping.core.networkx_grid_hamiltonian import gen_grid, hamiltonian_path_brute_force
from pydantic import BaseModel

class MapDimensions(BaseModel):
	height: float
	lenght: float

router = APIRouter()

@router.get("/trajectory/", tags = ["Trajectory"])
def get_trajectory_data():
	return {"message": "trajectory data"}

@router.post("/trajectory/", tags = ["Trajectory"])
def post_map_data(map_dimensions: MapDimensions):
	return {"message": "Trajectory generated", "status": "Success", "data": hamiltonian_path_brute_force(gen_grid(map_dimensions.height, map_dimensions.lenght))}

