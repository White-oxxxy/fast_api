from dataclasses import dataclass, field
from abc import ABC
from uuid import uuid4, UUID


@dataclass
class BaseEntity(ABC):
    oid: UUID = field(
        default_factory=lambda: uuid4(),
        kw_only=True,
    )

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, __value: "BaseEntity") -> bool:
        return self.oid == __value.oid