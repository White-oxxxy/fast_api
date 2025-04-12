from pathlib import Path
from pydantic_settings import SettingsConfigDict

from .config import *


class CommonSettings:
    database_settings: DatabaseSettings
    jwt_settings: JWTSettings


class DevSettings(CommonSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[2] / ".dev.env",
        env_file_encoding="utf-8",
        extra="allow",
    )


class ProdSettings(CommonSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[2] / ".prod.env",
        env_file_encoding="utf-8",
        extra="allow",
    )
