import re


def slugify(text):
    """Lowercase text and replace runs of non-alphanumerics with a dash."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower())
