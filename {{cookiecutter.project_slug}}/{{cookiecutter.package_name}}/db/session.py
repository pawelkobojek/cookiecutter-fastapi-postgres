from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.DB_URI, pool_pre_ping=True, echo=settings.ECHO_SQL_STATEMENTS)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
