from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import relationship

from api.src.database import Base

class sensores(Base):
    __tablename__ = "sensores"

    id = Column(Integer, primary_key = True, autoincrement = True)


class trajectory(Base):
    __tablename__ = "trajectory"

    id = Column(Integer, primary_key = True, autoincrement = True)
    height = Column(Float(precision = 6, decimal_return_scale = None), nullable = False)
    lenght = Column(Float(precision = 6, decimal_return_scale = None), nullable = False)