from fastapi import APIRouter
from mapping.core.networkx_grid_hamiltonian import gen_grid, hamiltonian_path_brute_force
from pydantic import BaseModel

class MapDimensions(BaseModel):
	height: float
	lenght: float

router = APIRouter()

database_simul = []

@router.get("/trajectory/", tags = ["Trajectory"])
def get_trajectory_data():
	return {"message": "trajectory data", "status": "Success", "data": database_simul}


@router.get("/trajectory/{id}", tags = ["Trajectory"])
def get_trajectory_data_with_id(id: int):
	return {"message": "trajectory data", "status": "Success", "data": database_simul[id]}


@router.post("/trajectory/", tags = ["Trajectory"])
def post_map_data(map_dimensions: MapDimensions):
	trajectory = hamiltonian_path_brute_force(gen_grid(map_dimensions.height, map_dimensions.lenght))
	database_simul.append(trajectory)

	return {"message": "Trajectory generated", "status": "Success", "data": trajectory}

