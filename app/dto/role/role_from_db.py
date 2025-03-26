from dataclasses import dataclass

from .creae_role import RoleCreate
from ..mixins import IntPkMixin, TimeMixin


@dataclass
class RoleFromDB(RoleCreate, IntPkMixin, TimeMixin): ...
