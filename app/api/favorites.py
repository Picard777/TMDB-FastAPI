from fastapi import APIRouter, HTTPException, Depends, status
from app.schemas.favorite import FavoriteCreate, FavoriteByTitleCreate
from app.schemas.favorite import FavoriteRead, FavoriteWithDetails
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db.deps import get_db
from app.models.favorite import FavoriteMovie
from app.services.tmdb_client import TMDBClient
from httpx import HTTPStatusError


router = APIRouter(prefix="/favorites", tags=["favorites"])

@router.get("/movies", response_model=list[FavoriteWithDetails])
async def get_favorite_movies(db: Session = Depends(get_db)):
    favorites = db.query(FavoriteMovie).all()
    tmdb_client = TMDBClient()
    
    results = []
    for fav in favorites:
        try:
            details = await tmdb_client.get_movie_details(fav.movie_id)
        except HTTPStatusError as e:
            details = {
                "error": "Movie not found in TMDB",
                "status_code": e.response.status_code
            }
        results.append({
            "id": fav.id,
            "movie_id": fav.movie_id,
            "details": details
        })
    return results

@router.post("/movies/by-title", response_model=FavoriteWithDetails)
async def add_favorite_by_title(
    payload: FavoriteByTitleCreate,
    db: Session = Depends(get_db)
):
    tmdb_client = TMDBClient()
    search_result = await tmdb_client.search_movies(payload.title)
    
    if not search_result["results"]:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    movie = search_result["results"][0]
    movie_id = movie["id"]
    
    db_favorite = FavoriteMovie(movie_id=movie_id)
    db.add(db_favorite)
    
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Movie already in favorites")
    
    db.refresh(db_favorite)
    details = await tmdb_client.get_movie_details(movie_id)
    
    return {
        "id": db_favorite.id,
        "movie_id": movie_id,
        "details": details
    }

@router.post("/movies/{movieid}", response_model=FavoriteRead, status_code=status.HTTP_201_CREATED, responses = {
    409: {
        "description": "Movie already in favorites"}
    }
)
def add_favorite_movie(
    favorite: FavoriteCreate,
    db: Session = Depends(get_db),
    ):
    db_favorite = FavoriteMovie(movie_id=favorite.movie_id)
    db.add(db_favorite)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Movie already in favorites"
        )
    db.refresh(db_favorite)
    return db_favorite

@router.delete("/movies/{movie_id}", status_code=204)
def remove_favorite_movie(
    movie_id: int, 
    db: Session = Depends(get_db)):
    db_favorite = db.query(FavoriteMovie).filter(
        FavoriteMovie.movie_id == movie_id
        ).first()
    if not db_favorite:
        raise HTTPException(status_code=404, detail="Favorite movie not found")
    db.delete(db_favorite)
    db.commit()
    
