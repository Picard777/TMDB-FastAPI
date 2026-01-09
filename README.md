# TMDB API

Backend API built with **FastAPI** that integrates with **The Movie Database (TMDB)** API  
and allows users to search movies and manage a list of favorite movies stored in **PostgreSQL**.

The project focuses on clean backend architecture, proper separation of concerns,
and real-world patterns such as database persistence, external API integration,
and Dockerized deployment.

---

## Tech stack

- **Python 3.11**
- **FastAPI**
- **Pydantic v2**
- **SQLAlchemy**
- **PostgreSQL**
- **Docker & Docker Compose**
- **TMDB API**

---

## Features

- Search movies using TMDB API
- Add movies to favorites
- Prevent duplicate favorites
- Persist data in PostgreSQL
- Fully Dockerized environment
- Interactive API documentation via Swagger

---

## Project structure
```
app/
├── api/            # FastAPI routers (favorites, search)
├── models/         # SQLAlchemy ORM models
├── schemas/        # Pydantic schemas (request / response)
├── services/       # External services (TMDB client)
├── db/             # Database session & dependencies
├── core/           # Configuration
└── main.py         # FastAPI app entrypoint
```
---

## Configuration

Create a `.env` file based on the example:

```
cp .env.example .env
DATABASE_URL=postgresql+psycopg2://tmdb:tmdb@db:5432/tmdb
TMDB_API_KEY=your_tmdb_api_key_here
DEBUG=false
```
## Running 
```
docker compose up --build
```
API will be available at:
	•	http://localhost:8000
	•	Swagger UI: http://localhost:8000/docs

## Planned Improvements
	•	Fetch full TMDB movie details for favorites
	•	Add automated tests (pytest)
	•	Pagination for search endpoints
	•	Improved error handling

## Author
Picard777
Aspiring Python Developer


