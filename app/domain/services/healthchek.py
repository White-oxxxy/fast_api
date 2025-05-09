from abc import ABC, abstractmethod


class IHealthCheckService(ABC):
    @abstractmethod
    async def execute(self) -> dict[str, bool]: ...
