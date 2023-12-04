from sqlalchemy import URL, create_engine,text
from config import settings

sync_engine=create_engine(
    url=settings.DATABASE_URL,
    echo=True,
)

async_engine=create_async_engine(
    url=settings.DATABASE_URL,
    echo=True,
)

with engine.connect() as conn: