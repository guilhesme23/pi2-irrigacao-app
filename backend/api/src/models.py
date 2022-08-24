from sqlalchemy import Column, ForeignKey, Integer, Float, TIMESTAMP, Enum, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict
import enum
from api.src.database import Base

class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    temp_air = Column(Float(precision = 6, decimal_return_scale = None), nullable = False)
    temp_soil = Column(Float(precision = 6, decimal_return_scale = None), nullable = False)
    humidity_air = Column(Float(precision = 6, decimal_return_scale = None), nullable = False)
    humidity_soil = Column(Float(precision = 6, decimal_return_scale = None), nullable = False)
    recorded_on = Column(DateTime(timezone=True), server_default=func.now())

class reports_enum(enum.Enum):
    INIT_CYCLE = 'INIT_CYCLE'
    END_CYCLE = 'END_CYCLE'
    LOW_BATTERY = 'LOW_BATTERY'

class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    battery_level = Column(Float(precision = 6, decimal_return_scale = None), nullable = False)
    remaining_points = Column(MutableDict.as_mutable(JSONB), nullable = False)
    recorded_on = Column(DateTime(timezone=True), server_default=func.now())
    status_report = Column(Enum(reports_enum), nullable = False)

class Field(Base):
    __tablename__ = "fields"

    id = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    field_width = Column(Float(precision = 6, decimal_return_scale = None), nullable = False)
    field_lenth = Column(Float(precision = 6, decimal_return_scale = None), nullable = False)
    routes = relationship("Route")

class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    base_pos_x = Column(Integer, nullable = False)
    base_pos_y = Column(Integer, nullable = False)
    irrigation_route = Column(MutableDict.as_mutable(JSONB), nullable=False)
    field_id = Column(Integer, ForeignKey("field.id"), nullable = False)

class irrigation_enum(enum.Enum):
    START = 'START'
    STOP = 'STOP'

class Irrigation(Base):
    __tablename__ = 'irrigation_commands'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    irrigate = Column(Enum(irrigation_enum), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
