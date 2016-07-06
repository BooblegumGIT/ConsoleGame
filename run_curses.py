from unicurses import *
from data.levels import LEVELS
from utilities import getchar, Clock
from data.objects import ICONS as OBJECTS_ICONS
from data.monsters import ICONS as MONSTERS_ICONS
from data.c_colors import *
from Classes.Hero import Hero
from data.status_bar import STATUS_BAR
from Classes.StatusBar import StatusBar


def render(field, status_bar):
    for i, line in enumerate(status_bar):
        # print(line)
        for j, obj in enumerate(line):
            mvaddch(i, j, CCHAR(obj))

    for i, line in enumerate(field, start=i+1):
        for j, obj in enumerate(line):
            mvaddch(i, j, *ICONS[obj]) if ICONS.get(obj) else mvaddstr(i, j, obj)

    mvaddstr(i + 4, 0, 'Key pressed {}'.format(key))


LEVEL = 1
FPS = 20
ICONS = {}
ICONS.update(OBJECTS_ICONS)
ICONS.update(MONSTERS_ICONS)

# INIT
stdscr = initscr()
start_color()
init_pairs()
# LINES, COLS = getmaxyx(stdscr)
if not has_colors():
    endwin()
    print("Your terminal does not support color!")
    exit(1)

clock = Clock()
field = LEVELS[LEVEL]
hero = Hero(char="H", field=field)
status_bar = StatusBar(STATUS_BAR, hero)
key = ''
render(field, status_bar.render())

while True:
    # clear()
    key = getchar(locked=False)
    if key == 'q':
        break
    hero.event(key)
    refresh()
    render(field, status_bar.render())
    clock.tick(FPS)
