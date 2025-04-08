from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from pydantic_settings import SettingsConfigDict

from .config import *


@dataclass
class CommonSettings:
    database_settings: DatabaseSettings
    jwt_settings: JWTSettings


@dataclass
class DevSettings(CommonSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[2] / ".dev.env",
        env_file_encoding="utf-8",
        extra="allow",
    )


@dataclass
class ProdSettings(CommonSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[2] / ".prod.env",
        env_file_encoding="utf-8",
        extra="allow",
    )


@lru_cache(1)
def get_settings(env: str = "dev") -> CommonSettings:
    db_settings = DatabaseSettings()
    jwt_settings = JWTSettings()
    match env:
        case "dev":
            return DevSettings(database_settings=db_settings, jwt_settings=jwt_settings)
        case "prod":
            return ProdSettings(database_settings=db_settings, jwt_settings=jwt_settings)
