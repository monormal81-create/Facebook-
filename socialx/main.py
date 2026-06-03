from fastapi import FastAPI

from database.database import Base
from database.database import engine

# ROUTERS
from app.auth.router import router as auth_router
from app.posts.router import router as posts_router
from app.follow.router import router as follow_router
app.include_router(follow_router)
from app.notifications.router import router as notifications_router
app.include_router(notifications_router)


# =========================
# CREATE DATABASE TABLES
# =========================

Base.metadata.create_all(bind=engine)


# =========================
# APP INSTANCE
# =========================

app = FastAPI(
    title="SocialX",
    version="0.1.0"
)


# =========================
# ROUTES REGISTRATION
# =========================

app.include_router(auth_router)
app.include_router(posts_router)


# =========================
# HEALTH CHECK
# =========================

@app.get("/")
def home():

    return {
        "project": "SocialX",
        "status": "running",
        "version": "0.1.0"
    }