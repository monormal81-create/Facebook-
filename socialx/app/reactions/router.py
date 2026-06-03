from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database.dependencies import get_db
from database.models import User

from app.auth.dependencies import get_current_user

from app.reactions.schemas import LikeCreate
from app.reactions.schemas import CommentCreate
from app.reactions.schemas import CommentResponse

from app.reactions.service import like_post
from app.reactions.service import comment_post


router = APIRouter(
    prefix="/reactions",
    tags=["Reactions"]
)


# =========================
# LIKE POST
# =========================

@router.post("/like")
def like(
    data: LikeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    try:

        return like_post(
            db=db,
            user=current_user,
            post_id=data.post_id
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# =========================
# COMMENT POST
# =========================

@router.post(
    "/comment",
    response_model=CommentResponse
)
def comment(
    data: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    try:

        return comment_post(
            db=db,
            user=current_user,
            post_id=data.post_id,
            content=data.content,
            parent_id=data.parent_id
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )