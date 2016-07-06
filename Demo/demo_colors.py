from unicurses import *

initscr()
start_color()

BG_COLOR = COLOR_BLACK
res = init_color(COLOR_GREEN, 200, 100, 0)

for n in range(16):
    init_pair(n, n, BG_COLOR)
    mvaddstr(n, 1, 'COLOR {}'.format(n), COLOR_PAIR(n))

refresh()
