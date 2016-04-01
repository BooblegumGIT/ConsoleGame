import tty
import termios
import sys
import os
import time

from data.colors import *
from data.objects import ICONS as OBJECTS_ICONS
from data.monsters import ICONS as MONSTERS_ICONS
from data.monsters import GAME_MONSTERS
from data.levels import LEVELS
from Classes.Hero import Hero
from Classes.StatusBar import StatusBar
from Classes.Monsters import MonsterCreator
from data.status_bar import STATUS_BAR
from data import objects

ICONS = {}
ICONS.update(OBJECTS_ICONS)
ICONS.update(MONSTERS_ICONS)
LEVEL = 0


def getchar():
    """
    Returns a single character from standard input
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def cls():
    """
    Очищаем консоль
    """
    os.system(['clear', 'cls'][os.name == 'nt'])


def render(field, status_bar):
    for line in status_bar:
        # render_line = ''
        # for char in line:
        #     render_line += ICONS[char] if ICONS.get(char) else char
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


def animation():
    level = LEVELS[LEVEL]
    char_temp = None
    for anim in animations_list[:]:
        for frame in anim["frames"]:
            if char_temp is None:
                char_temp = level[anim["pos"][1]][anim["pos"][0]]
            level[anim["pos"][1]][anim["pos"][0]] = frame
            cls()
            render(level, status_bar.render())
            time.sleep(anim["speed"])
        level[anim["pos"][1]][anim["pos"][0]] = char_temp
        cls()
        render(level, status_bar.render())
        char_temp = None
        animations_list.remove(anim)



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

while True:
    char = getchar()
    if char == 'q':
        break
    cls()
    hero.events(char)
    render(LEVELS[LEVEL], status_bar.render())
    time.sleep(0.2)
    cls()
    for monster in monsters[:]:
        monster.event("")
        if not monster.alive:
            monsters.remove(monster)
            hero.temp_current_tile_char = " "  # FIXME: костыль
            die_anim["pos"] = monster.pos.as_point()
            animations_list.append(die_anim)

    render(LEVELS[LEVEL], status_bar.render())
    if animations_list:
        time.sleep(2)
        animation()
    print('You pressed', char)
    # print(unit.key)
    # if unit.Hit_Points == 0 or unit.Hit_Points < 0:
    #     print('You die!!!')
    #     ch = 'q'
    # logs.render()