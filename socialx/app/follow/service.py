from sqlalchemy.orm import Session

from database.models import User
from database.models import Follow


# =========================
# FOLLOW USER
# =========================

def follow_user(db: Session, follower: User, following_id: int):

    if follower.id == following_id:
        raise ValueError("You cannot follow yourself")

    target_user = (
        db.query(User)
        .filter(User.id == following_id)
        .first()
    )

    if not target_user:
        raise ValueError("User not found")

    existing = (
        db.query(Follow)
        .filter(
            Follow.follower_id == follower.id,
            Follow.following_id == following_id
        )
        .first()
    )

    if existing:
        raise ValueError("Already following this user")

    follow = Follow(
        follower_id=follower.id,
        following_id=following_id
    )

    db.add(follow)
    db.commit()
    from app.notifications.service import send_notification
from app.notifications.service import create_notification
create_notification(
    db=db,
    user_id=following_id,
    from_user_id=follower.id,
    type="follow",
    message="started following you"
)
send_notification(
    user_id=followed_user_id,
    message="قام شخص بمتابعتك",
    notif_type="follow",
    from_user_id=follower_id
)
    return {"message": "Followed successfully"}


# =========================
# UNFOLLOW USER
# =========================

def unfollow_user(db: Session, follower: User, following_id: int):

    follow = (
        db.query(Follow)
        .filter(
            Follow.follower_id == follower.id,
            Follow.following_id == following_id
        )
        .first()
    )

    if not follow:
        raise ValueError("You are not following this user")

    db.delete(follow)
    db.commit()

    return {"message": "Unfollowed successfully"}


# =========================
# COUNTS
# =========================

def get_followers_count(db: Session, user_id: int):

    return (
        db.query(Follow)
        .filter(Follow.following_id == user_id)
        .count()
    )


def get_following_count(db: Session, user_id: int):

    return (
        db.query(Follow)
        .filter(Follow.follower_id == user_id)
        .count()
    )