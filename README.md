# chicago-smart-city-api

A modern FastAPI platform built on Chicago public datasets including CTA transit, restaurant inspections, and neighborhood analytics.

## Requirements

- Python 3.11+
- uv
- PostgreSQL
- Node.js 20+ (includes npm)

## Backend Setup

```bash
uv sync --dev
uv run uvicorn app.main:app --reload
```

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## Test and lint

```bash
uv run pytest
pre-commit run --all-files
```

## Project layout

```text
app/
  api/
    routes/             API route modules
      cta/              CTA endpoints
      health/           Health endpoints
      restaurant.../    Restaurant endpoints
  core/                 Application configuration
  db/
    models/             Database setup, session management, and models
  mappers/              Parsing functionality between models
  schemas/              Request and response schemas
  services/             Business logic and external data clients
    cta/                CTA data requests
    restaurants/
      chicago_client/   Requests for the City of Chicago API
      ingestion/        Ingestion service to postgresql
      queries/          Queries for the postgres database
frontend/               Frontend components using React with TypeScript
tests/                  Automated tests
```

## Roadmap

- CTA live arrivals
- Restaurant safety search
- CI/CD deployment
