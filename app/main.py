from fastapi import FastAPI
from app.api.search import router as search_router
from app.api.favorites import router as favorites_router
from app.db.session import engine
from app.db.base import Base




app = FastAPI(title="TMDB FastAPI")

Base.metadata.create_all(bind=engine)

app.include_router(search_router)
app.include_router(favorites_router)