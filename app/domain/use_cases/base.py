from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

CT = TypeVar("CT", bound=Any)  # command type
RT = TypeVar("RT", bound=Any)  # result type


class BaseUseCase(ABC, Generic[CT, RT]):
    @abstractmethod
    async def execute(self, command: CT) -> RT:
        pass
