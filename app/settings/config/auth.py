from dataclasses import dataclass
from datetime import timedelta
from typing import Optional, Union, Sequence
from pydantic import (
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
    field_validator,
)
from pydantic_settings import BaseSettings


@dataclass
class JWTSettings(BaseSettings):
    jwt_token_location: Optional[Sequence[StrictStr]] = Field(default="JWT_TOKEN_LOCATION", alias="JWT_TOKEN_LOCATION")
    jwt_public_key: Optional[StrictStr] = Field(default="JWT_PUBLIC_KEY", alias="JWT_PUBLIC_KEY")
    jwt_private_key: Optional[StrictStr] = Field(default="JWT_PRIVATE_KEY", alias="JWT_PRIVATE_KEY")
    jwt_algorithm: Optional[StrictStr] = Field(default="JWT_ALGORITHM", alias="JWT_ALGORITHM")
    jwt_decode_algorithms: Optional[StrictStr] = Field(default="JWT_DECODE_ALGORITHMS", alias="JWT_DECODE_ALGORITHMS")
    jwt_decode_leeway: Optional[Union[StrictInt, timedelta]] = 0
    jwt_encode_issuer: Optional[StrictStr] = Field(default="JWT_ENCODE_ISSUER", alias="JWT_ENCODE_ISSUER")
    jwt_decode_issuer: Optional[StrictStr] = Field(default="JWT_DECODE_ISSUER", alias="JWT_DECODE_ISSUER")
    jwt_header_name: Optional[StrictStr] = Field(default="JWT_HEADER_NAME", alias="JWT_HEADER_NAME")
    jwt_header_type: Optional[StrictStr] = Field(default="JWT_HEADER_TYPE", alias="JWT_HEADER_TYPE")
    jwt_access_token_expires: Optional[Union[StrictBool, StrictInt, timedelta]] = timedelta(minutes=15)
    jwt_refresh_token_expires: Optional[Union[StrictBool, StrictInt, timedelta]] = timedelta(days=30)

    jwt_access_cookie_key: Optional[StrictStr] = Field(default="JWT_ACCESS_COOKIE_KEY", alias="JWT_ACCESS_COOKIE_KEY")
    jwt_refresh_cookie_key: Optional[StrictStr] = Field(default="JWT_REFRESH_COOKIE_KEY", alias="JWT_REFRESH_COOKIE_KEY")
    jwt_access_cookie_path: Optional[StrictStr] = "/"
    jwt_refresh_cookie_path: Optional[StrictStr] = "/"
    jwt_cookie_max_age: Optional[StrictInt] = None
    jwt_cookie_domain: Optional[StrictStr] = None
    jwt_cookie_secure: Optional[StrictBool] = Field(default="JWT_COOKIE_SECURE", alias="JWT_COOKIE_SECURE")
    jwt_cookie_samesite: Optional[StrictStr] = Field(default="JWT_COOKIE_SAMESITE", alias="JWT_COOKIE_SAMESITE")

    jwt_cookie_csrf_protect: Optional[StrictBool] = Field(default="JWT_COOKIE_CSRF_PROTECT", alias="JWT_COOKIE_CSRF_PROTECT")
    jwt_access_csrf_cookie_key: Optional[StrictStr] = Field(default="JWT_ACCESS_CSRF_COOKIE_KEY", alias="JWT_ACCESS_CSRF_COOKIE_KEY")
    jwt_refresh_csrf_cookie_key: Optional[StrictStr] = Field(default="JWT_REFRESH_CSRF_COOKIE_KEY", alias="JWT_REFRESH_CSRF_COOKIE_KEY")
    jwt_access_csrf_cookie_path: Optional[StrictStr] = "/"
    jwt_refresh_csrf_cookie_path: Optional[StrictStr] = "/"
    jwt_access_csrf_header_name: Optional[StrictStr] = Field(default="JWT_ACCESS_CSRF_HEADER_NAME", alias="JWT_ACCESS_CSRF_HEADER_NAME")
    jwt_refresh_csrf_header_name: Optional[StrictStr] = Field(default="JWT_REFRESH_CSRF_HEADER_NAME", alias="JWT_REFRESH_CSRF_HEADER_NAME")
    jwt_csrf_methods: Optional[Sequence[StrictStr]] = Field(default="JWT_CSRF_METHODS", alias="JWT_CSRF_METHODS")

    @classmethod
    @field_validator('jwt_access_token_expires')
    def validate_access_token_expires(cls, v):
        if v is True:
            raise ValueError("'authjwt_access_token_expires' принимает только False, если недействителен") # noqa
        return v

    @classmethod
    @field_validator('jwt_refresh_token_expires')
    def validate_refresh_token_expires(cls, v):
        if v is True:
            raise ValueError("'authjwt_refresh_token_expires' принимает только False, если недействителен") # noqa
        return v

    @classmethod
    @field_validator('jwt_denylist_token_checks', mode='before')
    def validate_denylist_token_checks(cls, v):
        if v:
            for val in v:
                if val not in {"access", "refresh"}:
                    raise ValueError("'authjwt_denylist_token_checks' должен быть 'access' или 'refresh'") # noqa
        return v

    @classmethod
    @field_validator('jwt_token_location', mode='before')
    def validate_token_location(cls, v):
        if v:
            for val in v:
                if val not in {"headers", "cookies"}:
                    raise ValueError("'authjwt_token_location' должен быть 'headers' или 'cookies'") # noqa
        return v

    @classmethod
    @field_validator('jwt_cookie_samesite') # noqa
    def validate_cookie_samesite(cls, v):
        if v and v not in {"strict", "lax", "none"}:
            raise ValueError("'authjwt_cookie_samesite' должен быть 'strict', 'lax', или 'none'") # noqa
        return v

    @classmethod
    @field_validator('jwt_csrf_methods', mode='before')
    def validate_csrf_methods(cls, v):
        if v:
            return {method.upper() for method in v if method.upper() in {"GET", "HEAD", "POST", "PUT", "DELETE", "PATCH"}}
        return v

    @property
    def jwt_in_cookies(self) -> bool:
        return "cookies" in self.jwt_token_location

    @property
    def jwt_in_headers(self) -> bool:
        return "headers" in self.jwt_token_location

    class Config:
        min_anystr_length = 1
        anystr_strip_whitespace = True
        env_prefix = 'JWT_'