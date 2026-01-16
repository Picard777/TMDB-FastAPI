from pydantic import BaseModel, ConfigDict

class FavoriteCreate(BaseModel):
    movie_id: int
    
    
class FavoriteByTitleCreate(BaseModel):
    title: str
    
    
class FavoriteRead(BaseModel):
    id: int
    movie_id: int
    
    model_config = ConfigDict(from_attributes=True)


class FavoriteWithDetails(BaseModel):
    id: int
    movie_id: int
    details: dict | None
    
    model_config = ConfigDict(from_attributes=True)