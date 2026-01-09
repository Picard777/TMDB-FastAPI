from pydantic import BaseModel, ConfigDict

class FavoriteCreate(BaseModel):
    movie_id: int
    
class FavoriteRead(BaseModel):
    id: int
    movie_id: int
    
    model_config = ConfigDict(from_attributes=True)
