from sqlalchemy.orm import Session

from database.models import Group, GroupMember


# =========================
# CREATE GROUP
# =========================

def create_group(db: Session, name: str, description: str, owner_id: int):

    group = Group(
        name=name,
        description=description,
        owner_id=owner_id
    )

    db.add(group)
    db.commit()
    db.refresh(group)

    # add owner as member
    member = GroupMember(
        group_id=group.id,
        user_id=owner_id,
        role="owner"
    )

    db.add(member)
    db.commit()

    return group


# =========================
# JOIN GROUP
# =========================

def join_group(db: Session, group_id: int, user_id: int):

    exists = (
        db.query(GroupMember)
        .filter(GroupMember.group_id == group_id,
                GroupMember.user_id == user_id)
        .first()
    )

    if exists:
        return exists

    member = GroupMember(
        group_id=group_id,
        user_id=user_id,
        role="member"
    )

    db.add(member)
    db.commit()
    db.refresh(member)

    return member


# =========================
# LEAVE GROUP
# =========================

def leave_group(db: Session, group_id: int, user_id: int):

    member = (
        db.query(GroupMember)
        .filter(GroupMember.group_id == group_id,
                GroupMember.user_id == user_id)
        .first()
    )

    if member:
        db.delete(member)
        db.commit()

    return {"message": "left group"}


# =========================
# GET GROUP MEMBERS
# =========================

def get_group_members(db: Session, group_id: int):

    return (
        db.query(GroupMember)
        .filter(GroupMember.group_id == group_id)
        .all()
    )


# =========================
# GET GROUPS OF USER
# =========================

def get_user_groups(db: Session, user_id: int):

    return (
        db.query(GroupMember)
        .filter(GroupMember.user_id == user_id)
        .all()
    )