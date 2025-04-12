from cryptography.hazmat.primitives import serialization
from bcrypt import gensalt, hashpw, checkpw

def load_public_key(key: str):
    return serialization.load_der_public_key(key.encode())


def load_private_key(key: str):
    return serialization.load_pem_private_key(key.encode(), password=None)

def hash_password(
    password: str,
) -> bytes:
    salt = gensalt()
    pwd_bytes: bytes = password.encode()
    return hashpw(pwd_bytes, salt)

def validate_password(
    password: str,
    hashed_password: bytes,
) -> bool:
    return checkpw(
        password=password.encode(),
        hashed_password=hashed_password,
    )
