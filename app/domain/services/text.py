from abc import ABC, abstractmethod

from domain.entities.user import Text, Tag


class ITextService(ABC): ...


class ITagService(ABC): ...