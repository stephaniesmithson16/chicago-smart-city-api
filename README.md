# chicago-smart-city-api

A modern FastAPI platform built on Chicago public datasets including CTA transit, restaurant inspections, and neighborhood analytics.

## Tech Stack

## Requirements

- Python 3.11+
- uv

## Setup

```bash
uv sync --dev
```

## Run

```bash
uv run uvicorn app.main:app --reload
```

Or run the project script:

```bash
uv run chicago-smart-city-api
```

## Test and lint

```bash
uv run pytest
uv run ruff check .
```

## Project layout

```text
app/
  api/
    routes/         API route modules
  core/             Application configuration
  db/               Database setup and session management
    models/         Domain and persistence models
  mappers/          Parsing functionality between models
  schemas/          Request and response schemas
  services/         Business logic and external data clients
    cta/            CTA data requests
    restaurants/    Restaurant api requests, ingestion, and queries
tests/              Automated tests
```

## Roadmap

- CTA live arrivals
- Restaurant safety search
- CI/CD deployment
