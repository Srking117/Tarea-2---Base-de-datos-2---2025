"""Application configuration using Pydantic Settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Main application settings."""
    debug: bool = False
    jwt_secret_key: str = "secret123"
    database_url: str = "postgresql+psycopg://postgres:1234@localhost:5432/biblioteca_db_sebastian_riveros_k_umag_2025_v1"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()  