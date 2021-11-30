import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    """App configuration class."""

    class Config:
        secrets_dir = "/run/secrets"

    PROJECT_NAME: str = "{{cookiecutter.project_name}}"

    API_V1_PREFIX: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost", "http://localhost:8000"]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        """Supports JSON list, actual list, comma-separated list."""
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        if isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    ECHO_SQL_STATEMENTS: bool = True
    POSTGRES_HOST: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "{{cookiecutter.postgres_db_name}}"
    DB_URI: Optional[PostgresDsn] = None

    @validator("DB_URI", pre=True)
    def assemble_db_uri(cls, field_value: Optional[str], values: Dict[str, Any]) -> Any:
        """Assembles DB_URI from subarguments."""
        if isinstance(field_value, str):
            return field_value
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values["POSTGRES_HOST"],
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )


settings = Settings()
