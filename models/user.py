from typing import Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    password : str = Field(...)
    username : str = Field(...)
    email : str = Field(...)
    is_active : bool = Field(...)
    is_superuser : bool = Field(...)
    person : int = Field(...)