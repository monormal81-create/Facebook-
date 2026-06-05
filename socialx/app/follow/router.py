from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database.dependencies import get_db
from database.models import User

from app.auth.dependencies import get_current_user

from app.follow.schemas import FollowRequest
from app.follow.service import follow_user
from app.follow.service import unfollow_user
from app.follow.service import get_followers_count
from app.follow.service import get_following_count


router = APIRouter(
    prefix="/follow",
    tags=["Follow"]
)


# =========================
# FOLLOW
# =========================

@router.post("/")
def follow(
    data: FollowRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    try:

        return follow_user(
            db=db,
            follower=current_user,
            following_id=data.user_id
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# =========================
# UNFOLLOW
# =========================

@router.post("/unfollow")
def unfollow(
    data: FollowRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    try:

        return unfollow_user(
            db=db,
            follower=current_user,
            following_id=data.user_id
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# =========================
# FOLLOWERS COUNT
# =========================

@router.get("/followers/{user_id}")
def followers_count(
    user_id: int,
    db: Session = Depends(get_db)
):

    return {
        "followers": get_followers_count(db, user_id)
    }


# =========================
# FOLLOWING COUNT
# =========================

@router.get("/following/{user_id}")
def following_count(
    user_id: int,
    db: Session = Depends(get_db)
):

    return {
        "following": get_following_count(db, user_id)
    }