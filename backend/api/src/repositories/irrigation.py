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
    
    def get_current_irrigation_state(self) -> irrigation_enum:
        try:
            state = self.db.query(Irrigation).order_by(Irrigation.created_at.desc()).first()
            print(state)
            if state:
                return state.irrigate
        except:
            self.db.rollback()
            return irrigation_enum.STOP
