from enum import Enum


class Roles(Enum):
    DEFAULT_USER = 1
    ADMIN = 2

    @classmethod
    def from_id(cls, id_: int) -> str:
        for role in cls:
            if role.value == id_:
                return role.name.lower()
        raise ValueError(f"Неизвестный role_id: {id_}")

    @classmethod
    def to_id(cls, name: str) -> int:
        try:
            return cls[name.upper()].value
        except KeyError:
            raise ValueError(f"Неизвестное имя роли: {name}")
