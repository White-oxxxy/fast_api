from .base import AuthJWTException


class JWTDecodeException(AuthJWTException):
    def __init__(self, status_code: int, message: str):
        super().__init__(status_code, message)


