from sqlalchemy.orm import Session

from database.models import Page, PageFollower


# =========================
# CREATE PAGE
# =========================

def create_page(db: Session, name: str, description: str, category: str, owner_id: int):

    page = Page(
        name=name,
        description=description,
        category=category,
        owner_id=owner_id
    )

    db.add(page)
    db.commit()
    db.refresh(page)

    return page


# =========================
# FOLLOW PAGE
# =========================

def follow_page(db: Session, page_id: int, user_id: int):

    exists = (
        db.query(PageFollower)
        .filter(PageFollower.page_id == page_id,
                PageFollower.user_id == user_id)
        .first()
    )

    if exists:
        return exists

    follower = PageFollower(
        page_id=page_id,
        user_id=user_id
    )

    db.add(follower)
    db.commit()
    db.refresh(follower)

    return follower


# =========================
# UNFOLLOW PAGE
# =========================

def unfollow_page(db: Session, page_id: int, user_id: int):

    follower = (
        db.query(PageFollower)
        .filter(PageFollower.page_id == page_id,
                PageFollower.user_id == user_id)
        .first()
    )

    if follower:
        db.delete(follower)
        db.commit()

    return {"message": "unfollowed page"}


# =========================
# GET PAGE FOLLOWERS
# =========================

def get_page_followers(db: Session, page_id: int):

    return (
        db.query(PageFollower)
        .filter(PageFollower.page_id == page_id)
        .all()
    )


# =========================
# GET USER PAGES (owned)
# =========================

def get_user_pages(db: Session, user_id: int):

    return (
        db.query(Page)
        .filter(Page.owner_id == user_id)
        .all()
    )