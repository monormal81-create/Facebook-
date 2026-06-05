from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database.database import get_db

from app.analytics.service import (
    get_analytics,
    increase_views,
    refresh_analytics
)


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


# =========================
# GET ANALYTICS
# =========================

@router.get("/page/{page_id}")
def page_stats(
    page_id: int,
    db: Session = Depends(get_db)
):

    return get_analytics(db, page_id)


# =========================
# INCREASE VIEWS
# =========================

@router.post("/page/{page_id}/view")
def view_page(
    page_id: int,
    db: Session = Depends(get_db)
):

    return increase_views(db, page_id)


# =========================
# REFRESH ANALYTICS
# =========================

@router.post("/page/{page_id}/refresh")
def refresh(
    page_id: int,
    db: Session = Depends(get_db)
):

    return refresh_analytics(db, page_id)