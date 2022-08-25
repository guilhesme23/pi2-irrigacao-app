from pydantic import BaseModel

class FieldPost(BaseModel):
    width: float
    length: float

class FieldResponse(BaseModel):
    id: int
    field_width: float 
    field_length: float

    class Config:
        orm_mode = True

class CreateRoute(BaseModel):
    field_id: int
    base_pos_x: int = 0
    base_pos_y: int = 0

class RouteResponse(BaseModel):
    base_pos_x: int = 0
    base_pos_y: int = 0
    field_id: int
    irrigation_route: dict | list

    class Config:
        orm_mode = True
