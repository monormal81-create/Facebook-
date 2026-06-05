from sqlalchemy.orm import Session

from database.models import Conversation, Message

from app.realtime.manager import manager

import asyncio


# =========================
# GET OR CREATE CONVERSATION
# =========================

def get_or_create_conversation(
    db: Session,
    user1_id: int,
    user2_id: int
):

    conversation = (
        db.query(Conversation)
        .filter(
            (
                (Conversation.user1_id == user1_id)
                & (Conversation.user2_id == user2_id)
            )
            |
            (
                (Conversation.user1_id == user2_id)
                & (Conversation.user2_id == user1_id)
            )
        )
        .first()
    )

    if conversation:
        return conversation

    conversation = Conversation(
        user1_id=user1_id,
        user2_id=user2_id
    )

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return conversation


# =========================
# SEND MESSAGE
# =========================

def send_message(
    db: Session,
    conversation_id: int,
    sender_id: int,
    receiver_id: int,
    content: str
):

    message = Message(
        conversation_id=conversation_id,
        sender_id=sender_id,
        content=content,
        is_read=False
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    try:
        asyncio.create_task(
            manager.send_to_user(
                receiver_id,
                {
                    "type": "new_message",
                    "message_id": message.id,
                    "conversation_id": conversation_id,
                    "sender_id": sender_id,
                    "content": content,
                    "is_read": False
                }
            )
        )
    except Exception:
        pass

    return message


# =========================
# GET MESSAGES
# =========================

def get_messages(
    db: Session,
    conversation_id: int
):

    return (
        db.query(Message)
        .filter(
            Message.conversation_id == conversation_id
        )
        .order_by(Message.id.asc())
        .all()
    )


# =========================
# GET USER CONVERSATIONS
# =========================

def get_user_conversations(
    db: Session,
    user_id: int
):

    return (
        db.query(Conversation)
        .filter(
            (Conversation.user1_id == user_id)
            |
            (Conversation.user2_id == user_id)
        )
        .all()
    )


# =========================
# MARK MESSAGE AS READ
# =========================

def mark_message_as_read(
    db: Session,
    message_id: int
):

    message = (
        db.query(Message)
        .filter(Message.id == message_id)
        .first()
    )

    if message:
        message.is_read = True
        db.commit()

    return message