from typing import Optional
from pydantic import BaseModel, Field


class VehicleToPerson(BaseModel):
    vehicle_id : int = Field(...)
    person_id : int = Field(...)
    date : str = Field(...)
    active : bool = Field(...)

