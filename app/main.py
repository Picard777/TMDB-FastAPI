from fastapi import FastAPI
from app.api.movies import router as movies_router
from app.api.search import router as search_router
from app.api.favorites import router as favorites_router
from app.db.session import engine
from app.db.base import Base
import time
from app.models.favorite import FavoriteMovie
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="TMDB FastAPI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # DEV ONLY
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    retries = 5
    while retries:
        try:
            Base.metadata.create_all(bind=engine)
            print("Database connected")
            break
        except Exception as e:
            print("Waiting for database...")
            retries -= 1
            time.sleep(2)
    else:
        raise RuntimeError("Could not connect to the database")
        

app.include_router(search_router)
app.include_router(favorites_router)
app.include_router(movies_router)
