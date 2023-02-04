from typing import Optional
from pydantic import BaseModel, Field

class Person(BaseModel):
    # id: str = Field(alias="_id")
    name : str = Field(...)
    last_name : str = Field(...)
    date_of_birth : str = Field(...)
    identification : str = Field(...)
    profession : str = Field(...)
    married : bool = Field(...)
    monthly_income : float = Field(...)
    current_vehicle_id : str = Field(...)
    vehicules : list = Field(...)
