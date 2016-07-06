from data.c_colors import *


def do_door_closed(hero, obj_x, obj_y):
    if hero.keys:
        hero.keys -= 1
        hero.field[obj_y][obj_x] = "/"
    # return "I'm door closed"


def do_key(hero, obj_x, obj_y):
    hero.keys += 1
    hero.field[obj_y][obj_x] = " "


def do_heal(hero, obj_x, obj_y):
    hero.lives += 1
    hero.field[obj_y][obj_x] = " "


def do_treasure(hero, obj_x, obj_y):
    # ...
    hero.field[obj_y][obj_x] = " "


GAME_OBJECTS = [
    {"label": "Hero", "char": "H", "icon": BLUE('H'), "passable": True, "interactive": False, "do": None},
    {"label": "Wall", "char": "#", "icon": DARK_GRAY('#'), "passable": False, "interactive": False, "do": None},
    {"label": "Door_open", "char": "/", "icon": MAGENTA('/'), "passable": True, "interactive": False, "do": None},
    {"label": "Door_closed", "char": "|", "icon": MAGENTA('|'), "passable": False, "interactive": True,
     "do": do_door_closed},
    {"label": "Key", "char": "k", "icon": GREEN("k"), "passable": True, "interactive": True,
     "do": do_key},
    {"label": "Heal", "char": "e", "icon": RED("♥"), "passable": True, "interactive": True,
     "do": do_heal},
    {"label": "Treasure", "char": "t", "icon": LIGHT_YELLOW("T"), "passable": True, "interactive": True,
     "do": do_treasure},
    {"label": "Clover", "char": "c", "icon": GREEN("A"), "passable": True, "interactive": True,
     "do": do_treasure},
]

# Иконки объектов для отрисовки
ICONS = {obj['char']: obj["icon"] for obj in GAME_OBJECTS}

# Непроходимые объекты
IMPASSABLE_OBJECTS = [obj["char"] for obj in GAME_OBJECTS if not obj["passable"]]
# интерактивные объекты
INTERACTIVE_OBJECTS = [obj["char"] for obj in GAME_OBJECTS if obj["interactive"]]