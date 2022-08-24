from api.src.models import Irrigation, irrigation_enum
from sqlalchemy.orm import Session

class RepoIrrigation():
    def __init__(self, db: Session) -> None:
        self.db = db

    def set_irrigation_state(self, state: irrigation_enum) -> bool:
        print(state)
        try:
            self.db.add(Irrigation(irrigate=state))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False