from sqlalchemy.orm import Session

from database.models import Ad


# =========================
# CREATE AD
# =========================

def create_ad(
    db: Session,
    page_id: int,
    title: str,
    content: str,
    image: str,
    target_url: str,
    budget: int
):

    ad = Ad(
        page_id=page_id,
        title=title,
        content=content,
        image=image,
        target_url=target_url,
        budget=budget
    )

    db.add(ad)
    db.commit()
    db.refresh(ad)

    return ad


# =========================
# GET ACTIVE ADS
# =========================

def get_active_ads(db: Session):

    return (
        db.query(Ad)
        .filter(Ad.is_active == True)
        .all()
    )


# =========================
# INCREASE VIEWS
# =========================

def increase_ad_views(db: Session, ad_id: int):

    ad = db.query(Ad).filter(Ad.id == ad_id).first()

    if ad:
        ad.views += 1
        db.commit()

    return ad


# =========================
# INCREASE CLICKS
# =========================

def increase_ad_clicks(db: Session, ad_id: int):

    ad = db.query(Ad).filter(Ad.id == ad_id).first()

    if ad:
        ad.clicks += 1
        db.commit()

    return ad