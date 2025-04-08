from .base import AuthJWTException


class InvalidHeaderException(AuthJWTException):
    def __init__(self, status_code: int, message: str):
        super().__init__(status_code, message)


class JWTDecodeException(AuthJWTException):
    def __init__(self, status_code: int, message: str):
        super().__init__(status_code, message)


class CSRFException(AuthJWTException):
    def __init__(self, status_code: int, message: str):
        super().__init__(status_code, message)


class MissingTokenException(AuthJWTException):
    def __init__(self, status_code: int, message: str):
        super().__init__(status_code, message)


class RevokedTokenException(AuthJWTException):
    def __init__(self, status_code: int, message: str):
        super().__init__(status_code, message)


class AccessTokenRequiredException(AuthJWTException):
    def __init__(self, status_code: int, message: str):
        super().__init__(status_code, message)


class RefreshTokenRequiredException(AuthJWTException):
    def __init__(self, status_code: int, message: str):
        super().__init__(status_code, message)


class FreshTokenRequiredException(AuthJWTException):
    def __init__(self, status_code: int, message: str):
        super().__init__(status_code, message)