from dataclasses import dataclass

from domain.ports.healthchek import IDatabaseHealthchekPort
from domain.services.healthchek import IHealthCheckService


@dataclass
class PostgresHealthcheckService(IHealthCheckService):
    port: IDatabaseHealthchekPort

    async def execute(self) -> dict[str, bool]:
        result = await self.port.ping()
        return {self.__class__.__name__: result}