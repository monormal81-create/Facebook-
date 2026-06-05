import re


USERNAME_MIN_LENGTH = 3
USERNAME_MAX_LENGTH = 30

DISPLAY_NAME_MIN_LENGTH = 2
DISPLAY_NAME_MAX_LENGTH = 100

PASSWORD_MIN_LENGTH = 8


def validate_username(
    username: str
) -> None:
    """
    Validate username rules.
    """

    username = username.strip()

    if len(username) < USERNAME_MIN_LENGTH:
        raise ValueError(
            f"Username must be at least {USERNAME_MIN_LENGTH} characters."
        )

    if len(username) > USERNAME_MAX_LENGTH:
        raise ValueError(
            f"Username must not exceed {USERNAME_MAX_LENGTH} characters."
        )

    if " " in username:
        raise ValueError(
            "Username cannot contain spaces."
        )

    if not re.fullmatch(
        r"[a-zA-Z0-9_]+",
        username
    ):
        raise ValueError(
            "Username may contain only letters, numbers and underscore."
        )


def validate_display_name(
    display_name: str
) -> None:
    """
    Validate display name.
    """

    display_name = display_name.strip()

    if len(display_name) < DISPLAY_NAME_MIN_LENGTH:
        raise ValueError(
            f"Display name must be at least {DISPLAY_NAME_MIN_LENGTH} characters."
        )

    if len(display_name) > DISPLAY_NAME_MAX_LENGTH:
        raise ValueError(
            f"Display name must not exceed {DISPLAY_NAME_MAX_LENGTH} characters."
        )


def validate_email(
    email: str
) -> None:
    """
    Basic email validation.
    """

    email_pattern = (
        r"^[a-zA-Z0-9._%+-]+"
        r"@[a-zA-Z0-9.-]+"
        r"\.[a-zA-Z]{2,}$"
    )

    if not re.fullmatch(
        email_pattern,
        email
    ):
        raise ValueError(
            "Invalid email address."
        )


def validate_password(
    password: str
) -> None:
    """
    Password strength validation.
    """

    if len(password) < PASSWORD_MIN_LENGTH:
        raise ValueError(
            f"Password must be at least {PASSWORD_MIN_LENGTH}