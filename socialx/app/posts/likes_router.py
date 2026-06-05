from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database.database import get_db
from database.models import User

from app.auth.dependencies import get_current_user

from app.posts.likes_service import like_post


router = APIRouter(prefix="/likes", tags=["Likes"])


@router.post("/{post_id}")
def like(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return like_post(db, post_id, current_user.id)