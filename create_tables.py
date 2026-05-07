from app.db.base import Base
from app.db.models import restaurant  # noqa: F401
from app.db.session import engine

Base.metadata.create_all(bind=engine)
