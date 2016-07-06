import os
from data.colors import *
from data.objects import ICONS as OBJECTS_ICONS
from data.monsters import ICONS as MONSTERS_ICONS
from data.monsters import GAME_MONSTERS
from data.levels import LEVELS
from Classes.Hero import Hero
from Classes.StatusBar import StatusBar
from Classes.Monsters import MonsterCreator
from data.status_bar import STATUS_BAR
from utilities import getchar, cls, Clock

ICONS = {}
ICONS.update(OBJECTS_ICONS)
ICONS.update(MONSTERS_ICONS)
LEVEL = 0
FPS = 20


def render(field, status_bar):
    for line in status_bar:
        print(BG_BLUE(line))
    for line in field:
        render_line = ''
        for char in line:
            render_line += ICONS[char] if ICONS.get(char) else char
        print(BG_BLACK(render_line))
    print("Press 'q' to Exit")
    print(hero.lives)
    print("'a' ←")
    print("'d' →")
    print("'w' ↑")
    print("'s' ↓")


cls()
# Создаем игровые объекты
hero = Hero(char="H", field=LEVELS[LEVEL])  # FIXME: символ Героя должен выбираться автоматически из GAME_OBJECTS
status_bar = StatusBar(STATUS_BAR, hero)
monsters = MonsterCreator(LEVELS[LEVEL], GAME_MONSTERS, hero).monster_objects
# Отрисовываем
for monster in monsters:
    monster.come_back()
render(LEVELS[LEVEL], status_bar.render())
animations_list = []
die_anim = {"pos": None, "frames": [RED("●"), RED("◎"), RED("◯"), RED("◉")], 'speed': 0.2}
clock = Clock()
i = 0

while True:
    i += 1
    char = getchar(locked=False)
    # char = ''
    if char == 'q':
        break
    cls()
    hero.event(char)
    render(LEVELS[LEVEL], status_bar.render())
    cls()
    for monster in monsters[:]:
        monster.event("")
        if not monster.alive:
            monsters.remove(monster)
            hero.temp_current_tile_char = " "  # FIXME: костыль
            # die_anim["pos"] = monster.pos.as_point()
            # animations_list.append(die_anim)

    render(LEVELS[LEVEL], status_bar.render())
    clock.tick(FPS)
    # if animations_list:
    #     time.sleep(2)
    #     animation()
    print('You pressed', i, char)