from sqlalchemy.orm import Mapped, mapped_column, relationship
import sqlalchemy as sa
from datetime import datetime

from .base import BaseORM
from .mixins import TimeMixin, UUIDOidMixin, IntPKMixin
from .associative import TextTagORM


class TagORM(BaseORM, TimeMixin, UUIDOidMixin, IntPKMixin):
    __tablename__ = "tag" # noqa

    name: Mapped[str] = mapped_column(nullable=False)
    uploader_name: Mapped[str] = mapped_column(nullable=False)

    texts: Mapped[list["TextORM"]] = relationship(secondary=TextTagORM.__tablename__, back_populates="tags")


class TextORM(BaseORM, TimeMixin, UUIDOidMixin, IntPKMixin):
    __tablename__ = "text" # noqa

    value: Mapped[str] = mapped_column(nullable=False)
    uploader_name: Mapped[str] = mapped_column(nullable=False)

    tags: Mapped[list["TagORM"]] = relationship(secondary=TextTagORM.__tablename__, back_populates="texts")


class ActionORM(BaseORM, TimeMixin, UUIDOidMixin, IntPKMixin):
    __tablename__ = "action" # noqa

    content: Mapped[str] = mapped_column(nullable=False)
    author_name: Mapped[str] = mapped_column(nullable=False)


class UserORM(BaseORM, TimeMixin, UUIDOidMixin, IntPKMixin):
    __tablename__ = "user" # noqa

    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    role_id: Mapped[int] = mapped_column(sa.ForeignKey("role.id"))
    birthday: Mapped[datetime] = mapped_column(sa.DateTime, nullable=False)

    role: Mapped["RoleORM"] = relationship(back_populates="user")

class RoleORM(BaseORM, TimeMixin, IntPKMixin):
    __tablename__ = "role"  # noqa

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()

    user: Mapped[list["UserORM"]] = relationship(back_populates="role")
