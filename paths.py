import os

BASE_DIR = os.path.dirname(__file__)

ICONS_DIR = os.path.join(
    BASE_DIR,
    "resources",
    "icons"
)

def icon_path(file_name):
    return os.path.join(ICONS_DIR, file_name)