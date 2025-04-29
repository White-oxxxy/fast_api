from sqlalchemy.orm import Mapped, mapped_column, relationship
import sqlalchemy as sa
from datetime import datetime
from uuid import UUID

from .base import BaseORM
from .mixins import TimeMixin, UUIDOidMixin, IntPKMixin
from .associative import TextTagORM


class TagORM(BaseORM, TimeMixin, UUIDOidMixin):
    __tablename__ = "tag"  # noqa

    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    uploader_name: Mapped[str] = mapped_column(nullable=False)

    texts: Mapped[list["TextORM"]] = relationship(
        secondary=TextTagORM.__tablename__, back_populates="tags"
    )


class TextORM(BaseORM, TimeMixin, UUIDOidMixin):
    __tablename__ = "text"  # noqa

    value: Mapped[str] = mapped_column(nullable=False, unique=True)
    uploader_name: Mapped[str] = mapped_column(nullable=False)

    tags: Mapped[list["TagORM"]] = relationship(
        secondary=TextTagORM.__tablename__, back_populates="texts"
    )


class ActionORM(BaseORM, TimeMixin, UUIDOidMixin):
    __tablename__ = "action"  # noqa

    content: Mapped[str] = mapped_column(nullable=False)
    author_name: Mapped[str] = mapped_column(nullable=False)


class RefreshTokenORM(BaseORM, TimeMixin, UUIDOidMixin, IntPKMixin):
    __tablename__ = "refresh_tokens"  # noqa

    token: Mapped[str] = mapped_column(unique=True, nullable=False)
    user_oid: Mapped[UUID] = mapped_column(sa.ForeignKey("user.oid"))
    role_oid: Mapped[UUID] = mapped_column(sa.ForeignKey("role.oid"))
    user_agent: Mapped[str] = mapped_column()
    ip_address: Mapped[str] = mapped_column()
    expires_at: Mapped[datetime] = mapped_column(nullable=False)
    revoked: Mapped[bool] = mapped_column(default=False)

    user: Mapped["UserORM"] = relationship(back_populates="refresh_tokens")
    role: Mapped["RoleORM"] = relationship(back_populates="refresh_tokens")


class UserORM(BaseORM, TimeMixin, UUIDOidMixin):
    __tablename__ = "user"  # noqa

    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    role_id: Mapped[int] = mapped_column(sa.ForeignKey("role.pk"))
    email: Mapped[str] = mapped_column(nullable=False)
    birthday: Mapped[datetime] = mapped_column(sa.DateTime, nullable=False)

    refresh_tokens: Mapped["RefreshTokenORM"] = relationship(back_populates="user")
    role: Mapped["RoleORM"] = relationship(back_populates="user")


class RoleORM(BaseORM, TimeMixin, UUIDOidMixin):
    __tablename__ = "role"  # noqa

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()

    user: Mapped[list["UserORM"]] = relationship(back_populates="role")
