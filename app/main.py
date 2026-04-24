from fastapi import FastAPI

from app.routes import health


def create_app() -> FastAPI:
    app = FastAPI(
        title="Chicago Smart City API",
        summary="Civic-tech API built on Chicago open data sources.",
        version="0.1.0",
    )
    app.include_router(health.router, prefix="/api/v1")
    return app


app = create_app()
