from pydantic import BaseModel
from typing import List

class Patient(BaseModel):
    id: int
    name: str
    age: int
    medical_history: List[str]
