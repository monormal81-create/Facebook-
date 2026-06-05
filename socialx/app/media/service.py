from app.core.cloudinary import upload_image
from app.core.cloudinary import delete_image


# =========================
# UPLOAD PROFILE IMAGE
# =========================

def upload_profile_image(file):

    return upload_image(file, folder="profiles")


# =========================
# UPLOAD COVER IMAGE
# =========================

def upload_cover_image(file):

    return upload_image(file, folder="covers")


# =========================
# UPLOAD POST IMAGE
# =========================

def upload_post_image(file):

    return upload_image(file, folder="posts")