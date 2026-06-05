from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from pydantic import BaseModel

from database.schemas import UserCreate
from database.schemas import UserResponse

from database.dependencies import get_db

from app.auth.service import create_user
from app.auth.service import login_user


# =========================
# ROUTER
# =========================

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# =========================
# LOGIN MODEL
# =========================

class LoginRequest(BaseModel):
    email: str
    password: str


# =========================
# REGISTER
# =========================

@router.post("/register", response_model=UserResponse)
def register_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):

    try:
        return create_user(db, user_data)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# =========================
# LOGIN
# =========================

@router.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):

    try:
        return login_user(
            db=db,
            email=data.email,
            password=data.password
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )