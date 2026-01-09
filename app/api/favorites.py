from fastapi import APIRouter, HTTPException, Depends
from app.schemas.favorite import FavoriteCreate
from app.schemas.favorite import FavoriteRead
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.models.favorite import FavoriteMovie
from app.services.tmdb_client import TMDBClient


router = APIRouter(prefix="/favorites", tags=["favorites"])

@router.get("/movies", response_model=list[FavoriteCreate])
async def get_favorite_movies(db: Session = Depends(get_db)):
    favorites = db.query(FavoriteMovie).all()

    results = []
    for fav in favorites:
        details = await TMDBClient.get_movie_details(fav.movie_id)
        results.append({
            "movie_id": fav.movie_id,
            "details": details
        })
    return results

@router.post("/movies", response_model=FavoriteRead)
def add_favorite_movie(
    favorite: FavoriteCreate,
    db: Session = Depends(get_db),
    ):
    db_favorite = FavoriteMovie(movie_id=favorite.movie_id)
    db.add(db_favorite)
    try:
        db.commit()
    except Exception:
        db.rollback()
        raise HTTPException(status_code=409, detail="Movie already in favorites"
        )
    db.refresh(db_favorite)
    return db_favorite

@router.delete("/movies/{movie_id}", response_model=FavoriteCreate)
def remove_favorite_movie(movie_id: int, db: Session = Depends(get_db)):
    db_favorite = db.query(FavoriteMovie).filter(
        FavoriteMovie.movie_id == movie_id
        ).first()
    if not db_favorite:
        raise HTTPException(status_code=404, detail="Favorite movie not found")
    db.delete(db_favorite)
    db.commit()
    
