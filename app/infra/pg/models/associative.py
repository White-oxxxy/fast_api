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
