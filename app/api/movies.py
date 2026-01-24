from fastapi import APIRouter
from app.services.tmdb_client import TMDBClient
from app.schemas.movie import MovieSearchResponse

router = APIRouter(prefix="/movies", tags=["movies"])
client = TMDBClient()

@router.get("/popular", response_model=MovieSearchResponse)
async def get_popular_movies():
    data = await client.get_popular_movies()
    return MovieSearchResponse(results=data.get("results", []))

@router.get("/top-rated", response_model=MovieSearchResponse)
async def get_top_rated_movies():
    data = await client.get_top_rated_movies()
    return MovieSearchResponse(results=data.get("results", []))

@router.get("/trending")
async def get_trending():
    return await client.get_trending()

@router.get("/{movie_id}")
async def get_movie_details(movie_id: int):
    return await client.get_movie_details(movie_id)
