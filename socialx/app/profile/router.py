from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database.dependencies import get_db

from app.profile.schemas import ProfileResponse
from app.profile.service import get_profile
from app.profile.service import get_user_posts
from app.profile.service import get_profile_stats


router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


# =========================
# GET PROFILE
# =========================

@router.get("/{username}", response_model=ProfileResponse)
def profile(
    username: str,
    db: Session = Depends(get_db)
):

    try:

        return get_profile(db, username)

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


# =========================
# USER POSTS
# =========================

@router.get("/{username}/posts")
def user_posts(
    username: str,
    db: Session = Depends(get_db)
):

    user = get_profile(db, username)

    return get_user_posts(db, user.id)


# =========================
# PROFILE STATS
# =========================

@router.get("/{username}/stats")
def profile_stats(
    username: str,
    db: Session = Depends(get_db)
):

    user = get_profile(db, username)

    return get_profile_stats(db, user.id)