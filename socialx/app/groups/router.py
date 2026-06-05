from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database.database import get_db
from database.models import User

from app.auth.dependencies import get_current_user

from app.groups.service import (
    create_group,
    join_group,
    leave_group,
    get_group_members,
    get_user_groups
)


router = APIRouter(
    prefix="/groups",
    tags=["Groups"]
)


# =========================
# CREATE GROUP
# =========================

@router.post("/")
def create(
    name: str,
    description: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_group(db, name, description, current_user.id)


# =========================
# JOIN GROUP
# =========================

@router.post("/{group_id}/join")
def join(
    group_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return join_group(db, group_id, current_user.id)


# =========================
# LEAVE GROUP
# =========================

@router.post("/{group_id}/leave")
def leave(
    group_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return leave_group(db, group_id, current_user.id)


# =========================
# GROUP MEMBERS
# =========================

@router.get("/{group_id}/members")
def members(
    group_id: int,
    db: Session = Depends(get_db)
):

    return get_group_members(db, group_id)


# =========================
# USER GROUPS
# =========================

@router.get("/my")
def my_groups(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_user_groups(db, current_user.id)