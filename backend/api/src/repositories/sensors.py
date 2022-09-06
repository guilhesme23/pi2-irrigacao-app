from api.src.models import Sensor
from sqlalchemy.orm import Session


class RepoSensors():
    def __init__(self, db: Session) -> None:
        self.db = db

    def record_sensor_data(
        self,
        temp_air: float,
        temp_soil: float,
        humidity_air: float,
        humidity_soil: float
    ) -> Sensor:
        record = Sensor(temp=(temp_air, temp_soil), humidity=(humidity_air, humidity_soil))
        try:
            self.db.add(record)
            self.db.commit()
            return record
        except:
            self.db.rollback()
            raise
        
    def get_sensors_data(self) -> list[Sensor]:
        try:
            data = self.db.query(Sensor).order_by(Sensor.recorded_on.desc()).all()
            return data
        except:
            self.db.rollback()
            raise
