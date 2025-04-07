from dataclasses import dataclass
from pydantic_settings import BaseSettings
from pydantic import Field


@dataclass
class CommonSettings(BaseSettings):
    postgres_db: str = Field(default="POSTGRES_DB", alias="POSTGRES_DB")
    postgres_user: str = Field(default="POSTGRES_USER", alias="POSTGRES_USER")
    postgres_password: str = Field(
        default="POSTGRES_PASSWORD", alias="POSTGRES_PASSWORD"
    )
    port_db: str = Field(default="PORT_DB", alias="PORT_DB")
    host_db: str = Field(default="HOST_DB", alias="HOST_DB")
    private_key: str = Field(default="PRIVATE_KEY", alias="PRIVATE_KEY")
    public_key: str = Field(default="PUBLIC_KEY", alias="PUBLIC_KEY")
    algorithm: str = Field(default="ALGORITHM", alias="ALGORITHM")
    access_token_expire_min: str = Field(
        default="ACCESS_TOKE_EXPIRE_MIN", alias="ACCESS_TOKE_EXPIRE_MIN"
    )

    @property
    def postgres_url(self) -> str:
        return rf"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.host_db}:{self.port_db}/{self.postgres_db}"
