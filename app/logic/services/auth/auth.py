from dataclasses import dataclass

from domain.services.auth.auth import IAuthService
from utils.auth import (
    encode_jwt,
    decode_jwt,
    hash_password,
    validate_password,
)
