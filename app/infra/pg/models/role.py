from sqlalchemy.orm import Mapped, mapped_column, relationship

from infra.pg.models.base import BaseORM
from domain.entities.role import Role
from infra.pg.models.mixins import TimeMixin, UUIDOidMixin
from infra.pg.models.user import UserORM


class RoleORM(BaseORM, TimeMixin, UUIDOidMixin):
    __tablename__ = "role" # noqa

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()

    users: Mapped[list[UserORM]] = relationship(back_populates="role")

    @staticmethod
    def from_entity(entity: Role) -> "RoleORM":
        return RoleORM(
            oid=entity.oid,
            name=entity.name,
            description=entity.description
        )

    def to_entity(self) -> Role:
        return Role(
            oid=self.oid,
            name=self.name,
            description=self.description
        )