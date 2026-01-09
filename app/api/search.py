from fastapi import APIRouter, Query
from app.services.tmdb_client import TMDBClient
from app.schemas.movie import MovieSearchResponse
from app.schemas.person import PersonSearchResponse 

router = APIRouter(prefix="/search", tags=["search"])
client = TMDBClient()

@router.get("/movies")
async def search_movies(query: str = Query(..., min_length=1)):
    return await client.search_movies(query)
@router.get("/people")
async def search_people(query: str = Query(..., min_length=1)):
    return await client.search_people(query)

@router.get("/movies", response_model=MovieSearchResponse)
async def search_movies(query: str = Query(..., min_length=1)):
    data = await client.search_movies(query)
    return MovieSearchResponse(results=data.get("results", []))

@router.get("/people", response_model=PersonSearchResponse)
async def search_people(query: str = Query(..., min_length=1)):
    data = await client.search_people(query)
    return PersonSearchResponse(results=data.get("results", []))
