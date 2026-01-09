import os

DATABASE_URL = os.getenv("DATABASE_URL")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

DEBUG = os.getenv("DEBUG", "false").lower() == "true"
TMDB_BASE_URL = "https://api.themoviedb.org/3"
