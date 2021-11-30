from pydantic import PostgresDsn
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from {{cookiecutter.package_name}}.core.config import settings

SQLALCHEMY_DATABASE_URL = PostgresDsn.build(
    scheme="postgresql",
    user=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_HOST,
    path=f"/{settings.POSTGRES_DB}_test",
)
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, echo=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
