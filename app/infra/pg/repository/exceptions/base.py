from dataclasses import dataclass

from domain.exeptions.base import ApplicationException


@dataclass
class RepositoryException(ApplicationException):
    @property
    def message(self):
        return "Произошла ошибка в запросе!"