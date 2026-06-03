from sqlalchemy.orm import Session

from database.models import Like
from database.models import Comment
from database.models import Post
from database.models import User


# =========================
# LIKE POST
# =========================

def like_post(db: Session, user: User, post_id: int):
from app.notifications.service import create_notification
create_notification(
    db=db,
    user_id=post.user_id,
    from_user_id=user.id,
    type="like",
    message="liked your post",
    post_id=post_id
)
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise ValueError("Post not found")

    existing_like = (
        db.query(Like)
        .filter(
            Like.post_id == post_id,
            Like.user_id == user.id
        )
        .first()
    )

    if existing_like:
        raise ValueError("You already liked this post")

    like = Like(
        user_id=user.id,
        post_id=post_id
    )

    db.add(like)
    db.commit()

    return {"message": "Post liked successfully"}


# =========================
# COMMENT POST
# =========================

def comment_post(
    db: Session,
    user: User,
    post_id: int,
    content: str,
    parent_id: int = None
):

    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise ValueError("Post not found")

    if not content or len(content.strip()) == 0:
        raise ValueError("Comment cannot be empty")

    comment = Comment(
        user_id=user.id,
        post_id=post_id,
        content=content,
        parent_id=parent_id
    )

    db.add(comment)
    db.commit()
    db.refresh(comment)
from app.notifications.service import create_notification
create_notification(
    db=db,
    user_id=post.user_id,
    from_user_id=user.id,
    type="comment",
    message="commented on your post",
    post_id=post_id
)
    return comment