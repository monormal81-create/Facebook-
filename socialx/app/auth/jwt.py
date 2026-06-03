from datetime import datetime
from datetime import timedelta

from jose import jwt


# =========================
# CONFIG
# =========================

SECRET_KEY = "CHANGE_THIS_SECRET_KEY_TO_SOMETHING_SECURE"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 1 day


# =========================
# CREATE TOKEN
# =========================

def create_access_token(data: dict) -> str:
    """
    Generate JWT access token.
    """

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update(
        {"exp": expire}
    )

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# =========================
# DECODE TOKEN
# =========================

def decode_access_token(token: str) -> dict:
    """
    Decode JWT token.
    """

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except Exception:
        return None