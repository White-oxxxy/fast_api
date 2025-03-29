from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from uuid import UUID

from .base import BaseORM
from .mixins import TimeMixin


class TextTagORM(BaseORM, TimeMixin):
    __tablename__ = "tag_text"  # noqa

    tag_oid: Mapped[UUID] = mapped_column(
        ForeignKey("tag.oid"), nullable=False, primary_key=True
    )
    text_oid: Mapped[UUID] = mapped_column(
        ForeignKey("text.oid"), nullable=False, primary_key=True
    )


class UserTagORM(BaseORM, TimeMixin):
    __tablename__ = "user_tag" # noqa

    tag_id: Mapped[UUID] = mapped_column(
        ForeignKey("tag.oid"), nullable=False, primary_key=True
    )
    user_oid: Mapped[UUID] = mapped_column(
        ForeignKey("user.oid"), nullable=False, primary_key=True
    )


class UserTextORM(BaseORM, TimeMixin):
    __tablename__ = "user_text" # noqa

    text_oid: Mapped[UUID] = mapped_column(
        ForeignKey("text.oid"), nullable=False, primary_key=True
    )
    user_oid: Mapped[UUID] = mapped_column(
        ForeignKey("user.oid"), nullable=False, primary_key=True
    )


class UserActionORM(BaseORM, TimeMixin):
    __tablename__ = "user_action" # noqa

    action_oid: Mapped[UUID] = mapped_column(
        ForeignKey("action.oid"), nullable=False, primary_key=True
    )
    user_oid: Mapped[UUID] = mapped_column(
        ForeignKey("user.oid"), nullable=False, primary_key=True
    )