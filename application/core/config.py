from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings


class RunModel(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DataBaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    max_overflow: int = 10
    pool_size: int = 50


class Settings(BaseSettings):
    run: RunModel = RunModel()
    api: ApiPrefix = ApiPrefix()
    db: DataBaseConfig


settings = Settings()
