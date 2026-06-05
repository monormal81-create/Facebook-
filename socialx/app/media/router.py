from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database.database import get_db
from database.models import User

from app.auth.dependencies import get_current_user

from app.media.service import upload_profile_image
from app.media.service import upload_cover_image
from app.media.service import upload_post_image


router = APIRouter(
    prefix="/media",
    tags=["Media"]
)


# =========================
# PROFILE IMAGE
# =========================

@router.post("/upload/avatar")
def upload_avatar(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    result = upload_profile_image(file.file)

    current_user.avatar = result["url"]

    db.commit()

    return result


# =========================
# COVER IMAGE
# =========================

@router.post("/upload/cover")
def upload_cover(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    result = upload_cover_image(file.file)

    current_user.cover = result["url"]

    db.commit()

    return result


# =========================
# POST IMAGE
# =========================

@router.post("/upload/post")
def upload_post_image_route(
    file: UploadFile = File(...)
):

    result = upload_post_image(file.file)

    return result