from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Text

from datetime import datetime

from database.database import Base


# ==================================================
# USERS
# ==================================================

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    user_tag = Column(String(20), unique=True, index=True, nullable=False)

    username = Column(String(30), unique=True, index=True, nullable=False)

    display_name = Column(String(100), nullable=False)

    email = Column(String(255), unique=True, index=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    bio = Column(String(10000), default="")

    avatar = Column(String(500), default="")

    cover = Column(String(500), default="")

    theme = Column(String(50), default="default")

    is_verified = Column(Boolean, default=False)

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )


# ==================================================
# POSTS
# ==================================================

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, index=True, nullable=False)

    content = Column(Text, nullable=False)

    image = Column(String(500), nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )


# ==================================================
# LIKES
# ==================================================

class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, index=True)

    post_id = Column(Integer, index=True, nullable=False)

    user_id = Column(Integer, index=True, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )


# ==================================================
# COMMENTS
# ==================================================

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, index=True, nullable=False)

    post_id = Column(Integer, index=True, nullable=False)

    content = Column(Text, nullable=False)

    parent_id = Column(Integer, nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )


# ==================================================
# FOLLOWS
# ==================================================

class Follow(Base):
    __tablename__ = "follows"

    id = Column(Integer, primary_key=True, index=True)

    follower_id = Column(Integer, index=True, nullable=False)

    following_id = Column(Integer, index=True, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )


# ==================================================
# NOTIFICATIONS
# ==================================================

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, index=True, nullable=False)

    from_user_id = Column(Integer, index=True, nullable=False)

    type = Column(String(50), nullable=False)

    post_id = Column(Integer, nullable=True)

    message = Column(String(255), nullable=False)

    is_read = Column(Boolean, default=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )


# ==================================================
# HASHTAGS
# ==================================================

class Hashtag(Base):
    __tablename__ = "hashtags"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String(100),
        unique=True,
        index=True,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# ==================================================
# CONVERSATIONS
# ==================================================

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)

    user1_id = Column(Integer, index=True, nullable=False)

    user2_id = Column(Integer, index=True, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# ==================================================
# MESSAGES
# ==================================================

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)

    conversation_id = Column(Integer, index=True, nullable=False)

    sender_id = Column(Integer, index=True, nullable=False)

    content = Column(String(1000), nullable=False)

    is_read = Column(Boolean, default=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# ==================================================
# GROUPS
# ==================================================

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    description = Column(String(500), default="")

    owner_id = Column(Integer, index=True, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# ==================================================
# GROUP MEMBERS
# ==================================================

class GroupMember(Base):
    __tablename__ = "group_members"

    id = Column(Integer, primary_key=True, index=True)

    group_id = Column(Integer, index=True, nullable=False)

    user_id = Column(Integer, index=True, nullable=False)

    role = Column(String(20), default="member")

    joined_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# ==================================================
# PAGES
# ==================================================

class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    description = Column(String(500), default="")

    owner_id = Column(Integer, index=True, nullable=False)

    category = Column(String(50), default="general")

    avatar = Column(String(500), default="")

    cover = Column(String(500), default="")

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# ==================================================
# PAGE FOLLOWERS
# ==================================================

class PageFollower(Base):
    __tablename__ = "page_followers"

    id = Column(Integer, primary_key=True, index=True)

    page_id = Column(Integer, index=True, nullable=False)

    user_id = Column(Integer, index=True, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# ==================================================
# PRODUCTS
# ==================================================

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    page_id = Column(Integer, index=True, nullable=False)

    name = Column(String(100), nullable=False)

    description = Column(String(500), default="")

    price = Column(Integer, nullable=False)

    image = Column(String(500), default="")

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# ==================================================
# ORDERS
# ==================================================

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    product_id = Column(Integer, index=True, nullable=False)

    user_id = Column(Integer, index=True, nullable=False)

    quantity = Column(Integer, default=1)

    total_price = Column(Integer, nullable=False)

    status = Column(String(50), default="pending")

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# ==================================================
# PAGE ANALYTICS
# ==================================================

class PageAnalytics(Base):
    __tablename__ = "page_analytics"

    id = Column(Integer, primary_key=True, index=True)

    page_id = Column(Integer, index=True, nullable=False)

    views = Column(Integer, default=0)

    followers = Column(Integer, default=0)

    posts = Column(Integer, default=0)

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


# ==================================================
# ADS
# ==================================================

class Ad(Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True, index=True)

    page_id = Column(Integer, index=True, nullable=False)

    title = Column(String(200), nullable=False)

    content = Column(String(1000), nullable=False)

    image = Column(String(500), default="")

    target_url = Column(String(500), default="")

    budget = Column(Integer, default=0)

    views = Column(Integer, default=0)

    clicks = Column(Integer, default=0)

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )