import re


# =========================
# EXTRACT HASHTAGS
# =========================

def extract_hashtags(text: str):

    return re.findall(r"#(\w+)", text)


# =========================
# FORMAT HASHTAGS
# =========================

def format_hashtags(tags: list):

    return ",".join(tags)