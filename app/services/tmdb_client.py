import httpx
from app.core.config import TMDB_API_KEY, TMDB_BASE_URL

class TMDBClient:
    async def get_movie(self, movie_id: int):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{TMDB_BASE_URL}/movie/{movie_id}",
                params={"api_key": TMDB_API_KEY
                }
            )
            response.raise_for_status()
            return response.json()
        
    async def get_trending(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{TMDB_BASE_URL}/trending/all/week",
                params={"api_key": TMDB_API_KEY
                }
            )
            response.raise_for_status()
            return response.json()
        
    async def search_movies(self, query: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{TMDB_BASE_URL}/search/movie",
                params={"api_key": TMDB_API_KEY
                        , "query": query
                }
            )
            response.raise_for_status()
            return response.json()
        
    async def search_people(self, query: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{TMDB_BASE_URL}/search/person",
                params={"api_key": TMDB_API_KEY
                        , "query": query
                }
            )
            response.raise_for_status()
            return response.json()
        
    async def get_popular_movies(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{TMDB_BASE_URL}/movie/popular",
                params={"api_key": TMDB_API_KEY
                }
            )
            response.raise_for_status()
            return response.json()
        
    async def get_top_rated_movies(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{TMDB_BASE_URL}/movie/top_rated",
                params={"api_key": TMDB_API_KEY
                }
            )
            return response.json()
    
    async def get_movie_details(self, movie_id:int) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{TMDB_BASE_URL}/movie/{movie_id}",
                params = {"api_key": TMDB_API_KEY
                 }
            )
            response.raise_for_status()
            return response.json()
    
    