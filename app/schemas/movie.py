from pydantic import BaseModel
from typing import List, Optional

class Movie(BaseModel):
    id: int
    title: str
    overview: Optional[str]
    release_date: Optional[str]
    popularity: Optional[float]
    vote_average: Optional[float]
    vote_count: Optional[int]
    poster_path: Optional[str]
    
class MovieSearchResponse(BaseModel):
    results: List[Movie]
    
