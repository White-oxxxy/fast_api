from abc import ABC, abstractmethod


class IDatabaseHealthchekPort(ABC):
    @abstractmethod
    async def ping(self) -> bool: ...