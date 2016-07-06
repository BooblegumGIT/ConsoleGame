from data.colors import *
from Classes.Monsters import *

GAME_MONSTERS = [
    {"label": "snake", "char": "S", "icon": LIGHT_CYAN("S"), "class": Snake},
    {"label": "ghost", "char": "G", "icon": LIGHT_GRAY("G"), "class": Ghost},
]

ICONS = {obj['char']: obj["icon"] for obj in GAME_MONSTERS}

IMPASSABLE_OBJECTS = [obj["char"] for obj in GAME_MONSTERS]

INTERACTIVE_OBJECTS = [obj["char"] for obj in GAME_MONSTERS]