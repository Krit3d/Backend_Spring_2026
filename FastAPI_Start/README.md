# 🚀 Core API Service (FastAPI)

This module serves as the foundational backend architecture for future AI-agent integration and data orchestration. It is built with a focus on true asynchrony, modularity, and strict data validation.

## ⚙️ Tech Stack
- **Framework:** FastAPI
- **Database:** PostgreSQL (via `asyncpg` for high-performance non-blocking I/O)
- **Validation:** Pydantic V2 (`pydantic-settings` for configuration)
- **Server:** Uvicorn
- **Containerization:** Docker & Docker Compose

## 🏗️ Architectural Highlights
- **Connection Pooling:** A robust PostgreSQL connection pool is initialized at application startup (lifespan), ensuring efficient resource management and preventing connection exhaustion under high concurrency.
- **Separation of Concerns:** The application is strictly divided into routing (`routers/`), data validation (`schemas/`), and database logic (`database.py`).
- **Environment Management:** Sensitive data and configurations (like DB credentials) are securely managed via `.env` files and a dedicated `config.py` module.

## 📂 Project Structure

```text
FastAPI_Start/
│
├── app/
│   ├── routers/
│   │   ├── __init__.py
│   │   └── users.py        # API endpoints (GET, POST)
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── users.py        # Pydantic validation models
│   ├── config.py           # Environment variables validation
│   ├── database.py         # Asyncpg pool & SQL queries
│   └── main.py             # FastAPI app & pool init
│
├── .dockerignore           # Docker build exclusions
├── .env                    # Local env vars (DB credentials)
├── docker-compose.yml      # API & PostgreSQL orchestration
├── Dockerfile              # Container setup
├── README.md               # Local documentation
└── requirements.txt        # Python dependencies
```

## 🛠️ Quick Start
To run this app, ensure you have installed 'Docker Desktop' or similar.

**1. Clone the repository and navigate to the project directory:**
```bash
git clone https://github.com/Krit3d/backend-ai-engineering.git
cd FastAPI_Start
```

**2. Configure Environment Variables:**
Create a `.env` file in the root of the `FastAPI_Start` directory and configure your database credentials (ensure they match your `docker-compose.yml` configuration):
```env
POSTGRES_HOST=db     # Use 'db' if running inside docker-network, or 'localhost'
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=fastapi_db
```

**3. Build and run the containers:**
```bash
docker-compose up -d --build
```
*The API will be available at `http://127.0.0.1:8000` and the Postgres database will be running in the background.*

## Run Locally (For Development)
If you prefer to run the FastAPI app directly on your host machine, ensure you have an active PostgreSQL instance running locally.

**1. Setup your virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Configure `.env`:**
Set `DB_HOST=localhost` in your `.env` file to point to your local PostgreSQL instance.

**4. Start the server:**
```bash
uvicorn app.main:app --reload
```

## 📡 API Documentation
Once the server is running, FastAPI automatically generates interactive API documentation.
- **Swagger UI:** Navigate to `http://127.0.0.1:8000/docs` in your browser to test endpoints directly.
- **ReDoc:** Navigate to `http://127.0.0.1:8000/redoc` for alternative documentation formatting.