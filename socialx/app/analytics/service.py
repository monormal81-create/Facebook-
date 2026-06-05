from sqlalchemy.orm import Session

from database.models import PageAnalytics, PageFollower, Post


# =========================
# GET OR CREATE ANALYTICS
# =========================

def get_or_create_analytics(db: Session, page_id: int):

    analytics = (
        db.query(PageAnalytics)
        .filter(PageAnalytics.page_id == page_id)
        .first()
    )

    if analytics:
        return analytics

    analytics = PageAnalytics(
        page_id=page_id,
        views=0,
        followers=0,
        posts=0
    )

    db.add(analytics)
    db.commit()
    db.refresh(analytics)

    return analytics


# =========================
# UPDATE PAGE VIEWS
# =========================

def increase_views(db: Session, page_id: int):

    analytics = get_or_create_analytics(db, page_id)

    analytics.views += 1

    db.commit()

    return analytics


# =========================
# REFRESH ANALYTICS
# =========================

def refresh_analytics(db: Session, page_id: int):

    analytics = get_or_create_analytics(db, page_id)

    followers_count = (
        db.query(PageFollower)
        .filter(PageFollower.page_id == page_id)
        .count()
    )

    posts_count = (
        db.query(Post)
        .filter(Post.user_id == page_id)  # لاحقًا يمكن تحسينها
        .count()
    )

    analytics.followers = followers_count
    analytics.posts = posts_count

    db.commit()

    return analytics


# =========================
# GET ANALYTICS
# =========================

def get_analytics(db: Session, page_id: int):

    return get_or_create_analytics(db, page_id)