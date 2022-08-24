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
            print(field)
            return field
        except:
            self.db.rollback()
            raise
