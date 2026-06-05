from sqlalchemy.orm import Session

from database.models import User
from database.schemas import UserCreate

from app.auth.security import hash_password
from app.auth.security import verify_password

from app.auth.jwt import create_access_token

from app.auth.validators import (
    validate_username,
    validate_display_name,
    validate_email,
    validate_password
)


# =========================
# USER TAG GENERATOR
# =========================

def generate_user_tag(db: Session) -> str:
    """
    Generate sequential SocialX tag.
    Example: SX000001
    """

    last_user = (
        db.query(User)
        .order_by(User.id.desc())
        .first()
    )

    if not last_user:
        return "SX000001"

    return f"SX{last_user.id + 1:06d}"


# =========================
# CHECKERS
# =========================

def is_username_taken(db: Session, username: str) -> bool:
    return (
        db.query(User)
        .filter(User.username == username)
        .first()
        is not None
    )


def is_email_taken(db: Session, email: str) -> bool:
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
        is not None
    )


# =========================
# REGISTER
# =========================

def create_user(db: Session, user_data: UserCreate) -> User:

    # Validation
    validate_username(user_data.username)
    validate_display_name(user_data.display_name)
    validate_email(user_data.email)
    validate_password(user_data.password)

    # Duplicates
    if is_username_taken(db, user_data.username):
        raise ValueError("Username already exists")

    if is_email_taken(db, user_data.email):
        raise ValueError("Email already exists")

    # Create user
    user = User(
        user_tag=generate_user_tag(db),
        username=user_data.username,
        display_name=user_data.display_name,
        email=user_data.email,
        password_hash=hash_password(user_data.password),
        bio="",
        avatar="",
        cover="",
        theme="default",
        is_verified=False,
        is_active=True
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# =========================
# LOGIN
# =========================

def login_user(db: Session, email: str, password: str):

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        raise ValueError("Invalid email or password")

    if not verify_password(password, user.password_hash):
        raise ValueError("Invalid email or password")

    token = create_access_token(
        data={
            "user_id": user.id,
            "user_tag": user.user_tag,
            "username": user.username
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": user
    }