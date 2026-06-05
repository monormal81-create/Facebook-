from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database.database import get_db

from app.search.service import search_users
from app.search.service import search_posts
from app.search.service import search_hashtag


router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


# =========================
# SEARCH USERS
# =========================

@router.get("/users")
def users(q: str, db: Session = Depends(get_db)):

    return search_users(db, q)


# =========================
# SEARCH POSTS
# =========================

@router.get("/posts")
def posts(q: str, db: Session = Depends(get_db)):

    return search_posts(db, q)


# =========================
# SEARCH HASHTAGS
# =========================

@router.get("/hashtags/{tag}")
def hashtags(tag: str, db: Session = Depends(get_db)):

    return search_hashtag(db, tag)