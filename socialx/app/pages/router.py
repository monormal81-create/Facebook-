from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database.database import get_db
from database.models import User

from app.auth.dependencies import get_current_user

from app.pages.service import (
    create_page,
    follow_page,
    unfollow_page,
    get_page_followers,
    get_user_pages
)


router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)


# =========================
# CREATE PAGE
# =========================

@router.post("/")
def create(
    name: str,
    description: str,
    category: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_page(db, name, description, category, current_user.id)


# =========================
# FOLLOW PAGE
# =========================

@router.post("/{page_id}/follow")
def follow(
    page_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return follow_page(db, page_id, current_user.id)


# =========================
# UNFOLLOW PAGE
# =========================

@router.post("/{page_id}/unfollow")
def unfollow(
    page_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return unfollow_page(db, page_id, current_user.id)


# =========================
# PAGE FOLLOWERS
# =========================

@router.get("/{page_id}/followers")
def followers(
    page_id: int,
    db: Session = Depends(get_db)
):

    return get_page_followers(db, page_id)


# =========================
# USER PAGES
# =========================

@router.get("/my")
def my_pages(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_user_pages(db, current_user.id)