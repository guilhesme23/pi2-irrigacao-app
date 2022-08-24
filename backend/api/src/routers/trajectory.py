from fastapi import APIRouter
from fastapi.params import Depends
from mapping.core.networkx_grid_route import christofides_tsp_custom, gen_grid
from pydantic import BaseModel

from api.src.database import engine, get_db
import api.src.models as models
from sqlalchemy.orm import Session

router = APIRouter()

class MapDimensions(BaseModel):
	height: float
	lenght: float

	class Config:
		schema_extra = {
			"example": {
				"height": 12.2,
				"lenght": 23.1,
			}
		}


models.Base.metadata.create_all(bind=engine)

@router.get("/trajectory/", tags = ["Trajectory"])
def get_trajectory_data(db:Session = Depends(get_db)):
	all_trajectories = db.query(models.trajectory).all()

	return {"message": "trajectory data", "status": "Success", "data": all_trajectories}


@router.get("/trajectory/{id}", tags = ["Trajectory"])
def get_trajectory_data_with_id(id: int, db:Session = Depends(get_db)):
	trajectory_data = db.query(models.trajectory).filter(models.trajectory.id == id).first()
	return {"message": "trajectory data", "status": "Success", "data": trajectory_data}


@router.post("/trajectory/", tags = ["Trajectory"])
def post_map_data(map_dimensions: MapDimensions, db:Session = Depends(get_db)):
	new_trajectory = models.trajectory(**map_dimensions.dict())
	trajectory = christofides_tsp_custom(gen_grid(map_dimensions.height, map_dimensions.lenght))
	db.add(new_trajectory)
	db.commit()
	db.refresh(new_trajectory)
	print(trajectory)

	return {"message": "Trajectory generated", "status": "Success", "data": new_trajectory}
