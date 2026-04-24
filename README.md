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
  core/       Application configuration
  models/     Domain and persistence models
  routes/     API route modules
  schemas/    Request and response schemas
  services/   Business logic and external data clients
tests/        Automated tests
```

## Roadmap

- CTA live arrivals
- Restaurant safety search
- Neighborhood metrics
- CI/CD deployment
