from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database.database import get_db

from app.auth.dependencies import get_current_user
from database.models import User

from app.messages.service import (
    get_or_create_conversation,
    send_message,
    get_messages,
    get_user_conversations
)


router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)


# =========================
# CREATE / GET CONVERSATION
# =========================

@router.post("/conversation/{user_id}")
def create_conversation(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_or_create_conversation(
        db,
        current_user.id,
        user_id
    )


# =========================
# SEND MESSAGE
# =========================

@router.post("/{conversation_id}")
def create_message(
    conversation_id: int,
    content: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return send_message(
        db,
        conversation_id,
        current_user.id,
        content
    )


# =========================
# GET MESSAGES
# =========================

@router.get("/{conversation_id}")
def list_messages(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_messages(db, conversation_id)


# =========================
# GET CONVERSATIONS
# =========================

@router.get("/")
def list_conversations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_user_conversations(db, current_user.id)