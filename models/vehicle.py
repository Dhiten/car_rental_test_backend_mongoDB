from typing import Optional
from pydantic import BaseModel, Field

class Vehicle(BaseModel):
    brand : str = Field(...)
    model : str = Field(...)
    doors : int = Field(...)
    vehicle_type : str = Field(...)
    plate : str = Field(...)
    people : list = Field(...)