from sqlalchemy.orm import Mapped, mapped_column, relationship
import sqlalchemy as sa
from datetime import datetime

from .base import BaseORM
from .mixins import TimeMixin, UUIDOidMixin, IntPKMixin
from .associative import TextTagORM, UserTagORM, UserTextORM, UserActionORM


class TagORM(BaseORM, TimeMixin, UUIDOidMixin, IntPKMixin):
    __tablename__ = "tag" # noqa

    name: Mapped[str] = mapped_column(nullable=False)
    uploader_id: Mapped[int] = mapped_column(sa.ForeignKey("user.id"))

    user: Mapped[list["UserORM"]] = relationship(secondary=UserTagORM.__tablename__, back_populates="tag")
    texts: Mapped[list["TextORM"]] = relationship(secondary=TextTagORM.__tablename__, back_populates="tags")


class TextORM(BaseORM, TimeMixin, UUIDOidMixin, IntPKMixin):
    __tablename__ = "text" # noqa

    value: Mapped[str] = mapped_column(nullable=False)
    uploader_id: Mapped[int] = mapped_column(sa.ForeignKey("user.id"))

    user: Mapped[list["UserORM"]] = relationship(secondary=UserTextORM.__tablename__, back_populates="text")
    tags: Mapped[list["TagORM"]] = relationship(secondary=TextTagORM.__tablename__, back_populates="texts")


class ActionORM(BaseORM, TimeMixin, UUIDOidMixin, IntPKMixin):
    __tablename__ = "action" # noqa

    content: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(sa.ForeignKey("user.id"))

    user: Mapped[list["UserORM"]] = relationship(secondary=UserActionORM.__tablename__, back_populates="action")


class UserORM(BaseORM, TimeMixin, UUIDOidMixin, IntPKMixin):
    __tablename__ = "user" # noqa

    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    role_id: Mapped[int] = mapped_column(sa.ForeignKey("role.id"))
    birthday: Mapped[datetime] = mapped_column(sa.DateTime, nullable=False)

    text: Mapped[list["TextORM"]] = relationship(secondary=UserTextORM.__tablename__, back_populates="user")
    tag: Mapped[list["TagORM"]] = relationship(secondary=UserTagORM.__tablename__, back_populates="user")
    action: Mapped[list["ActionORM"]] = relationship(secondary=UserActionORM.__tablename__, back_populates="user")
    role: Mapped["RoleORM"] = relationship(back_populates="user")

class RoleORM(BaseORM, TimeMixin, UUIDOidMixin, IntPKMixin):
    __tablename__ = "role"  # noqa

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()

    user: Mapped[list["UserORM"]] = relationship(back_populates="role")
