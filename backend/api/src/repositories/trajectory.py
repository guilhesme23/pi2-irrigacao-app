from sqlalchemy.orm import Session
from api.src.models import Field, Route


class RepoRoute():
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_trajectory(
        self,
        base_pos_x: int,
        base_pos_y: int,
        trajectory: dict | list,
        field_id: int
    ) -> Route:
        route = Route(
            base_pos_x=base_pos_x,
            base_pos_y=base_pos_y,
            field_id=field_id,
            irrigation_route=trajectory
        )
        try:
            self.db.add(route)
            self.db.commit()
            return route
        except:
            self.db.rollback()

    def get_latest_trajectory(self):
        try:
            result = self.db.query(Field, Route).order_by(Field.id.desc()).filter(Field.id == Route.field_id).first()
            return result
        except:
            self.db.rollback()
            return None
