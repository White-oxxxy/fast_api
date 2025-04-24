from dataclasses import dataclass

from domain.services.healthchek import IHealthCheckService
from utils.aio import gather_and_wait


@dataclass
class CompositeHealthcheckService(IHealthCheckService):
    services: list[IHealthCheckService]

    async def execute(self) -> dict[str, bool]:
        results = await gather_and_wait([service.execute() for service in self.services])

        ans = {}
        for result in results:
            ans.update(result)

        return ans