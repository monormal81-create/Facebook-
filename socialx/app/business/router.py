from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database.database import get_db
from database.models import User

from app.auth.dependencies import get_current_user

from app.business.service import (
    create_product,
    buy_product,
    get_page_products
)


router = APIRouter(
    prefix="/business",
    tags=["Business"]
)


# =========================
# CREATE PRODUCT
# =========================

@router.post("/product")
def create(
    page_id: int,
    name: str,
    description: str,
    price: int,
    image: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_product(db, page_id, name, description, price, image)


# =========================
# BUY PRODUCT
# =========================

@router.post("/buy/{product_id}")
def buy(
    product_id: int,
    quantity: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return buy_product(db, product_id, current_user.id, quantity)


# =========================
# GET PRODUCTS
# =========================

@router.get("/page/{page_id}")
def products(
    page_id: int,
    db: Session = Depends(get_db)
):

    return get_page_products(db, page_id)