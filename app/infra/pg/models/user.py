from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime
from datetime import datetime

from uuid import UUID

from domain.entities.user import User
from infra.pg.models.base import BaseORM
from infra.pg.models.role import RoleORM
from infra.pg.models.mixins import TimeMixin, UUIDOidMixin


class UserORM(BaseORM, TimeMixin, UUIDOidMixin):
    __tablename__ = "user" # noqa

    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    role_id: Mapped[UUID] = mapped_column(ForeignKey("role.oid"))
    birthday: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    role: Mapped[RoleORM] = relationship(back_populates="users")

    @staticmethod
    def from_entity(entity: User) -> "UserORM":
        return UserORM(
            oid=entity.oid,
            username=entity.username,
            password=entity.password,
            role_id=entity.role_id,
            birthday=entity.birthday
        )

    def to_entity(self) -> User:
        return User(
            oid=self.oid,
            username=self.username,
            password=self.password,
            role_id=self.role_id,
            birthday=self.birthday
        )