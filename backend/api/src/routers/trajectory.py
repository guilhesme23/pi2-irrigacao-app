from fastapi import APIRouter
from mapping.core.networkx_grid_hamiltonian import gen_grid, hamiltonian_path_brute_force
router = APIRouter()

@router.get("/trajectory/")
def get_sensors_data():
	return {"message": "trajectory data"}



