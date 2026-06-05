from sqlalchemy.orm import Session

from database.models import Product, Order, PageAnalytics


# =========================
# CREATE PRODUCT
# =========================

def create_product(db: Session, page_id: int, name: str, description: str, price: int, image: str):

    product = Product(
        page_id=page_id,
        name=name,
        description=description,
        price=price,
        image=image
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


# =========================
# BUY PRODUCT
# =========================

def buy_product(db: Session, product_id: int, user_id: int, quantity: int):

    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise ValueError("Product not found")

    total = product.price * quantity

    order = Order(
        product_id=product_id,
        user_id=user_id,
        quantity=quantity,
        total_price=total
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order


# =========================
# GET PAGE PRODUCTS
# =========================

def get_page_products(db: Session, page_id: int):

    return (
        db.query(Product)
        .filter(Product.page_id == page_id)
        .all()
    )