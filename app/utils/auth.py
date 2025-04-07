from datetime import datetime, timedelta

import bcrypt
import jwt

from settings.dev import DevSettings, get_settings


settings: DevSettings = get_settings()


def encode_jwt(
    payload: dict,
    private_key: settings.private_key,
    algorithm: settings.algorithm,
    expire_minutes: settings.access_token_expire_min,
    expire_timedelta: timedelta | None = None,
) -> str:
    to_encode = payload.copy()
    now = datetime.utcnow()
    if expire_timedelta:
        expire: datetime = now + expire_timedelta
    else:
        expire: datetime = now + timedelta(minutes=expire_minutes)

    to_encode.update(
        exp=expire,
        iat=now,
    )

    encoded = jwt.encode(
        to_encode, private_key.replace("\\n", "\n"), algorithm=algorithm
    )

    return encoded


def decode_jwt(
    token: str | bytes, public_key: settings.public_key, algorithm: settings.algorithm
) -> dict:
    decoded = jwt.decode(token, public_key.replace("\\n", "\n"), algorithms=[algorithm])
    return decoded


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


def validate_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password=password.encode(), hashed_password=hashed_password)
