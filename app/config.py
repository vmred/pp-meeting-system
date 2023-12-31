from pydantic import BaseModel
from yaml import Loader, load

from constants import config_path


class DatabaseConfig(BaseModel):
    host: str
    port: int
    username: str
    password: str
    db_name: str

    def connection_string(self) -> str:
        return f"postgresql+asyncpg://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}"


class ApplicationConfig(BaseModel):
    main_database: DatabaseConfig


def _load_config() -> ApplicationConfig:
    with open(config_path, "r", encoding='UTF-8') as f:
        config_data = load(f.read(), Loader)
    return ApplicationConfig(**config_data)


config = _load_config()
