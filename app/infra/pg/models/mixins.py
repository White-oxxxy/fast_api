from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, func


class TimeMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
        server_default=func.now(),
        onupdate=datetime.now(timezone.utc),
        server_onupdate=func.now(),
    )


class UUIDOidMixin:
    oid: Mapped[UUID] = mapped_column(primary_key=True, unique=True, default=uuid4)


class IntPKMixin:
    pk: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)