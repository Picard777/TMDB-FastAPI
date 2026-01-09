from pydantic import BaseModel
from typing import List, Optional

class Person(BaseModel):
    id: int
    name: str
    popularity: Optional[float]
    profile_path: Optional[str]
    
class PersonSearchResponse(BaseModel):
    results: List[Person]
