from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime
from datetime import datetime

from uuid import UUID

from .base import BaseORM
from .mixins import TimeMixin, UUIDOidMixin
from .associative import UserActionORM, UserTagORM, UserTextORM, TextTagORM


class TagORM(BaseORM, TimeMixin, UUIDOidMixin):
    __tablename__ = "tag" # noqa

    name: Mapped[str] = mapped_column(nullable=False)
    uploader_name: Mapped[list["UserORM"]] = relationship(back_populates="user")

    texts: Mapped[list["TextORM"]] = relationship(secondary=TextTagORM.__tablename__,back_populates="tags")


class TextORM(BaseORM, TimeMixin, UUIDOidMixin):
    __tablename__ = "text" # noqa

    value: Mapped[str] = mapped_column(nullable=False)

    tags: Mapped[list["TagORM"]] = relationship(secondary=TextTagORM.__tablename__,back_populates="texts")


class ActionORM(BaseORM, TimeMixin, UUIDOidMixin):
    __tablename__ = "action" # noqa

    content: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[list["UserORM"]] = relationship(secondary=UserActionORM.__tablename__, back_populates="action_author")


class UserORM(BaseORM, TimeMixin, UUIDOidMixin):
    __tablename__ = "user" # noqa

    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped["RoleORM"] = relationship(back_populates="users")
    birthday: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    action_author: Mapped[list["ActionORM"]] = relationship(secondary=UserActionORM.__tablename__, back_populates="author")
    # заебало


class RoleORM(BaseORM, TimeMixin, UUIDOidMixin):
    __tablename__ = "role"  # noqa

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()

    users: Mapped[list["UserORM"]] = relationship(back_populates="role")
