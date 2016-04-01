from data.colors import *
from Classes.Monsters import *

GAME_MONSTERS = [
    {"label": "snake", "char": "S", "icon": LIGHT_CYAN("☡"), "class": Snake},
    {"label": "snake", "char": "K", "icon": BLUE("😺"), "class": Cat},
    {"label": "ghost", "char": "G", "icon": LIGHT_GRAY("ⶇ"), "class": Ghost},
]

ICONS = {obj['char']: obj["icon"] for obj in GAME_MONSTERS}

IMPASSABLE_OBJECTS = [obj["char"] for obj in GAME_MONSTERS]

INTERACTIVE_OBJECTS = [obj["char"] for obj in GAME_MONSTERS]