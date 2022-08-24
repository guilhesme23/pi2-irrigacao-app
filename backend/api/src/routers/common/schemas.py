from pydantic import BaseModel

class FieldPost(BaseModel):
    width: float
    length: float

class FieldResponse(BaseModel):
    field_width: float 
    field_length: float

    class Config:
        orm_mode = True
