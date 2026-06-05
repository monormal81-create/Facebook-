from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database.dependencies import get_db
from database.schemas import PostResponse

from app.auth.dependencies import get_current_user
from database.models import User

from app.posts.schemas import PostCreate
from app.posts.service import create_post
from app.posts.service import get_posts
from app.posts.service import get_global_feed
from app.posts.service import get_following_feed
from app.auth.dependencies import get_current_user
from database.models import User
from app.posts.schemas import PostUpdate

from app.posts.service import update_post
from app.posts.service import delete_post


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


# =========================
# CREATE POST
# =========================

@router.post("/", response_model=PostResponse)
def add_post(
    data: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    try:

        return create_post(
            db=db,
            user=current_user,
            content=data.content,
            image=data.image
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# =========================
# GET FEED
# =========================

@router.get("/", response_model=list[PostResponse])
def feed(
    db: Session = Depends(get_db)
):

    return get_posts(db)
    @router.get("/feed/global")
def global_feed(
    db: Session = Depends(get_db)
):

    return get_global_feed(db)
    @router.get("/feed/following")
def following_feed(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_following_feed(
        db=db,
        user_id=current_user.id
    )
    # =========================
# UPDATE POST
# =========================

@router.put("/{post_id}")
def edit_post(
    post_id: int,
    data: PostUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    try:

        return update_post(
            db=db,
            post_id=post_id,
            user=current_user,
            content=data.content,
            image=data.image
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# =========================
# DELETE POST
# =========================

@router.delete("/{post_id}")
def remove_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    try:

        return delete_post(
            db=db,
            post_id=post_id,
            user=current_user
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )