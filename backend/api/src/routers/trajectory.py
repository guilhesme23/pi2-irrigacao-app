from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from mapping.core.networkx_grid_route import christofides_tsp_custom, gen_grid

from api.src.database import get_db
import api.src.models as models
from api.src.routers.common.schemas import CreateRoute, RouteResponse, FullTrajectoryResponse
from api.src.repositories import RepoFields, RepoRoute
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/trajectory/", tags=["Trajectory"], response_model=FullTrajectoryResponse)
def get_trajectory_data(db: Session = Depends(get_db)):
	repo = RepoRoute(db)
	trajectory = repo.get_latest_trajectory()
	if not trajectory:
		raise HTTPException(404, "Trajectory not found")

	return FullTrajectoryResponse(field=trajectory[0], route=trajectory[1])


@router.get("/trajectory/{id}", tags=["Trajectory"])
def get_trajectory_data_with_id(id: int, db: Session = Depends(get_db)):
	trajectory_data = db.query(models.trajectory).filter(
		models.trajectory.id == id).first()
	return {"message": "trajectory data", "status": "Success", "data": trajectory_data}


@router.post("/trajectory/", tags=["Trajectory"], response_model=RouteResponse)
def post_map_data(data: CreateRoute, db: Session = Depends(get_db)):
	field_repo = RepoFields(db)
	trajectory_repo = RepoRoute(db)
	field = field_repo.get_field_by_id(data.field_id)
	if not field:
		raise HTTPException(404, "Field not found")

	grid = gen_grid(field.field_width, field.field_length, [])
	trajectory = christofides_tsp_custom(
		grid, (data.base_pos_x, data.base_pos_y))

	route = {
		'irrigation_route': trajectory
	}

	res = trajectory_repo.create_trajectory(
		data.base_pos_x,
		data.base_pos_y,
		trajectory=route,
		field_id=data.field_id
	)
	return res
