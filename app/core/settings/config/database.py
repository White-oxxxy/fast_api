from dataclasses import dataclass
from pydantic_settings import BaseSettings
from pydantic import Field


@dataclass
class DatabaseSettings(BaseSettings):
    postgres_db: str = Field(default="POSTGRES_DB", alias="POSTGRES_DB")
    postgres_user: str = Field(default="POSTGRES_USER", alias="POSTGRES_USER")
    postgres_password: str = Field(
        default="POSTGRES_PASSWORD", alias="POSTGRES_PASSWORD"
    )
    port_db: str = Field(default="PORT_DB", alias="PORT_DB")
    master_host_db: str = Field(default="MASTER_HOST_DB", alias="MASTER_HOST_DB")
    slave_host_db: str = Field(default="SLAVE_HOST_DB", alias="SLAVE_HOST_DB")

    @property
    def master_postgres_url(self) -> str:
        return rf"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.master_host_db}:{self.port_db}/{self.postgres_db}"

    @property
    def slave_postgres_url(self) -> str:
        return rf"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.slave_host_db}:{self.port_db}/{self.postgres_db}"