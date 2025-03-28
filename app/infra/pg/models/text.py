from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from uuid import UUID

from domain.entities.text import Tag, Text
from infra.pg.models.base import BaseORM
from infra.pg.models.user import UserORM
from infra.pg.models.mixins import TimeMixin, UUIDOidMixin


class TagORM(BaseORM, TimeMixin, UUIDOidMixin):
    __tablename__ = "tag" # noqa

    name: Mapped[str] = mapped_column(nullable=False)
    uploader_id: Mapped[UUID] = mapped_column(ForeignKey("user.oid"))

    user: Mapped[list["UserORM"]] = relationship(back_populates="tags", secondary="text_tag")

    @staticmethod
    def from_entity(entity: Tag) -> "TagORM":
        ...

    def to_entity(self) -> Tag:
        ...


class TextORM(BaseORM, TimeMixin, UUIDOidMixin):
    __tablename__ = "text" # noqa
