from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment (.env supported)."""

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="MYPKG_", case_sensitive=False
    )

    DATABASE_URL: str = "sqlite:///./mypkg.db"
