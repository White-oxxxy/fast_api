from dataclasses import dataclass


@dataclass
class InfrastructureException(Exception):
    @property
    def message(self):
        return "Произошла ошибка обработки запроса!"