from pydantic import BaseModel
from typing import List

class UserSchema(BaseModel):
    name : str

class UserUpdateSchema(BaseModel):
    name: str
