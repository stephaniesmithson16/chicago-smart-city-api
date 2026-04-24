# chicago-smart-city-api

FastAPI civic-tech platform built on Chicago open data sources.

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
