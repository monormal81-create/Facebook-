from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database.database import get_db
from database.models import User

from app.auth.dependencies import get_current_user

from app.ads.service import (
    create_ad,
    get_active_ads,
    increase_ad_views,
    increase_ad_clicks
)


router = APIRouter(
    prefix="/ads",
    tags=["Ads"]
)


# =========================
# CREATE AD
# =========================

@router.post("/")
def create(
    page_id: int,
    title: str,
    content: str,
    image: str,
    target_url: str,
    budget: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_ad(
        db,
        page_id,
        title,
        content,
        image,
        target_url,
        budget
    )


# =========================
# GET ADS (FOR FEED)
# =========================

@router.get("/")
def ads(db: Session = Depends(get_db)):

    return get_active_ads(db)


# =========================
# VIEW AD
# =========================

@router.post("/{ad_id}/view")
def view(ad_id: int, db: Session = Depends(get_db)):

    return increase_ad_views(db, ad_id)


# =========================
# CLICK AD
# =========================

@router.post("/{ad_id}/click")
def click(ad_id: int, db: Session = Depends(get_db)):

    return increase_ad_clicks(db, ad_id)