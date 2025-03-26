from dataclasses import dataclass

from .create_user import UserCreate
from ..mixins import IntPkMixin, TimeMixin


@dataclass
class UserFromDB(UserCreate, IntPkMixin, TimeMixin): ...
