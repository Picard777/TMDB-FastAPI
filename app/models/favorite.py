from sqlalchemy import Column, Integer, DateTime, UniqueConstraint
from datetime import datetime
from app.db.base import Base

class FavoriteMovie(Base):
    __tablename__ = "favorites"
    
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    _table_args__ = (
        UniqueConstraint("movie_id", name="uq_favorite_movie_id"),
        )
