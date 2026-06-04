from fastapi import FastAPI

from database.database import Base
from database.database import engine


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
from app.auth.router import router as auth_router
from app.posts.router import router as posts_router
from app.follow.router import router as follow_router
app.include_router(follow_router)
from app.notifications.router import router as notifications_router
app.include_router(notifications_router)
from app.media.router import router as media_router

app.include_router(media_router)
from app.search.router import router as search_router

app.include_router(search_router)
from app.messages.router import router as messages_router

app.include_router(messages_router)
from app.groups.router import router as groups_router

app.include_router(groups_router)
from app.pages.router import router as pages_router

app.include_router(pages_router)
from app.business.router import router as business_router

app.include_router(business_router)
from app.analytics.router import router as analytics_router

app.include_router(analytics_router)
from app.ads.router import router as ads_router

app.include_router(ads_router)
from app.realtime.router import router as realtime_router

app.include_router(realtime_router)
from app.posts.likes_router import router as likes_router


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