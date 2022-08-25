from api.src.models import Field, Route
from sqlalchemy.orm import Session


class RepoFields():
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_field(self, width: float, length: float) -> Field:
        try:
            field = Field(field_width=width, field_length=length)
            self.db.add(field)
            self.db.commit()
            return field
        except:
            self.db.rollback()
            raise

    def get_fields(self) -> list[Field]:
        results = self.db.query(Field).order_by(Field.id.desc()).all()
        return results

    def get_field_by_id(self, id: int) -> Field | None:
        result = self.db.query(Field).filter(Field.id == id).first()
        return result
