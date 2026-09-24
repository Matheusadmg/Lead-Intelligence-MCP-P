from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class AppConfig(BaseSettings):

    # Configurações da Aplicação
    APP_NAME: str = "Lead Intelligence"
    APP_HOST: str
    APP_PORT: int
    APP_RELOAD: bool

    # Configurações do Banco de Dados
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int
    POSTGRES_HOST: str
    POSTGRES_ECHO: bool
    DB_DRIVER: str = "postgresql+asyncpg"

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"{self.DB_DRIVER}://" +
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@" +
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@lru_cache
def get_settings() -> AppConfig:
    return AppConfig()