from dataclasses import dataclass

from application.api.user.schemas.user import CreateUserSchema
from dto.user.user_response import User as UserDto


@dataclass
class FastAPIRequestToUserDto:
    @staticmethod
    def execute(request: CreateUserSchema) -> UserDto:
        return UserDto(
            username=request.username,
            password=request.password,
            email=request.email,
            birthday=request.birthday,
            role=request.role
        )

