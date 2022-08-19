from sqlalchemy import Column, ForeignKey, Integer, Float, JSON, TIMESTAMP, Enum
from sqlalchemy.orm import relationship
import enum
from api.src.database import Base

class sensors(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    temp_air = Column(Float(precision = 6, decimal_return_scale = None), nullable = False)
    temp_soil = Column(Float(precision = 6, decimal_return_scale = None), nullable = False)
    humidity_air = Column(Float(precision = 6, decimal_return_scale = None), nullable = False)
    humidity_soil = Column(Float(precision = 6, decimal_return_scale = None), nullable = False)
    recorded_on = Column(TIMESTAMP, nullable = False)

class reports_enum(enum.Enum):
    INIT_CYCLE = 'INIT_CYCLE'
    END_CYCLE = 'END_CYCLE'
    LOW_BATTERY = 'LOW_BATTERY'

class reports(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    battery_level = Column(Float(precision = 6, decimal_return_scale = None), nullable = False)
    remaining_points = Column(JSON, nullable = False)
    recorded_on = Column(TIMESTAMP, nullable = False)
    status_report = Column(Enum(reports_enum), nullable = False)

class field(Base):
    __tablename__ = "field"

    id = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    field_width = Column(Float(precision = 6, decimal_return_scale = None), nullable = False)
    field_lenth = Column(Float(precision = 6, decimal_return_scale = None), nullable = False)
    route = relationship("Child")

class route(Base):
    __tablename__ = "route"

    id = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    base_pos_x = Column(Integer, nullable = False)
    base_pos_y = Column(Integer, nullable = False)
    irrigation_route = Column(JSON, nullable = False)
    field_id = Column(Integer, ForeignKey("field.id"), nullable = False)
    