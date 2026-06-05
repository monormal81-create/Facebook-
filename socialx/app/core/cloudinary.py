import cloudinary
import cloudinary.uploader
import cloudinary.api

import os


# =========================
# CONFIG CLOUDINARY
# =========================

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)


# =========================
# UPLOAD IMAGE FUNCTION
# =========================

def upload_image(file, folder: str = "socialx"):

    result = cloudinary.uploader.upload(
        file,
        folder=folder
    )

    return {
        "url": result.get("secure_url"),
        "public_id": result.get("public_id")
    }


# =========================
# DELETE IMAGE FUNCTION
# =========================

def delete_image(public_id: str):

    return cloudinary.uploader.destroy(public_id)