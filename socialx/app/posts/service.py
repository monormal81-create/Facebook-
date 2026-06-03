from sqlalchemy.orm import Session

from database.models import User
from database.models import Post  # سنضيفه لاحقًا في models.py

from app.auth.dependencies import get_current_user


# =========================
# CREATE POST
# =========================

def create_post(
    db: Session,
    user: User,
    content: str,
    image: str = None
):

    if not content or len(content.strip()) == 0:
        raise ValueError("Post content cannot be empty")

    post = Post(
        user_id=user.id,
        content=content,
        image=image
    )

    db.add(post)
    db.commit()
    db.refresh(post)

    return post


# =========================
# GET FEED
# =========================

def get_posts(db: Session):

    posts = (
        db.query(Post)
        .order_by(Post.id.desc())
        .all()
    )

    return posts
    from sqlalchemy.orm import Session

from database.models import Post
from database.models import Follow


# =========================
# GLOBAL FEED
# =========================

def get_global_feed(db: Session):

    posts = (
        db.query(Post)
        .order_by(Post.id.desc())
        .all()
    )

    return posts


# =========================
# FOLLOWING FEED (IMPORTANT)
# =========================

def get_following_feed(db: Session, user_id: int):

    # get all users that current user follows
    following_ids = (
        db.query(Follow.following_id)
        .filter(Follow.follower_id == user_id)
        .all()
    )

    # convert tuples -> list
    following_ids = [f[0] for f in following_ids]

    if not following_ids:
        return []

    posts = (
        db.query(Post)
        .filter(Post.user_id.in_(following_ids))
        .order_by(Post.id.desc())
        .all()
    )

    return posts
    from datetime import datetime

from database.models import Like
from database.models import Comment
from database.models import Follow


def calculate_post_score(post, likes_count: int, comments_count: int) -> float:

    now = datetime.utcnow()

    # عمر المنشور بالساعات
    hours_old = (now - post.created_at).total_seconds() / 3600

    # كلما كان أحدث = نقاط أعلى
    time_score = max(0, 100 - hours_old)

    # التفاعل
    engagement_score = (likes_count * 2) + (comments_count * 3)

    return time_score + engagement_score
    def get_ranked_feed(db, user_id: int):

    # الأشخاص الذين يتابعهم المستخدم
    following_ids = (
        db.query(Follow.following_id)
        .filter(Follow.follower_id == user_id)
        .all()
    )

    following_ids = [f[0] for f in following_ids]

    posts = db.query(Post).all()

    ranked_posts = []

    for post in posts:

        likes_count = (
            db.query(Like)
            .filter(Like.post_id == post.id)
            .count()
        )

        comments_count = (
            db.query(Comment)
            .filter(Comment.post_id == post.id)
            .count()
        )

        score = calculate_post_score(
            post,
            likes_count,
            comments_count
        )

        # تعزيز لمن تتابعهم
        if post.user_id in following_ids:
            score += 50

        ranked_posts.append((post, score))

    # ترتيب حسب الأعلى
    ranked_posts.sort(key=lambda x: x[1], reverse=True)

    return [p[0] for p in ranked_posts]