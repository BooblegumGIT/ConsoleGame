from unicurses import *

BG_COLOR = COLOR_BLACK

GRAY = lambda s: (CCHAR(s), PD_COLOR_PAIR(0))
DARK_BLUE = lambda s: (CCHAR(s), PD_COLOR_PAIR(1))
GREEN = lambda s: (CCHAR(s), PD_COLOR_PAIR(2))
CYAN = lambda s: (CCHAR(s), PD_COLOR_PAIR(3))
RED = lambda s: (CCHAR(s), PD_COLOR_PAIR(4))
MAGENTA = lambda s: (CCHAR(s), PD_COLOR_PAIR(5))
YELLOW = lambda s: (CCHAR(s), PD_COLOR_PAIR(6))
WHITE = lambda s: (CCHAR(s), PD_COLOR_PAIR(7))
DARK_GRAY = lambda s: (CCHAR(s), PD_COLOR_PAIR(8))
BLUE = lambda s: (CCHAR(s), PD_COLOR_PAIR(9))
LIGHT_GREEN = lambda s: (CCHAR(s), PD_COLOR_PAIR(10))
LIGHT_BLUE = lambda s: (CCHAR(s), PD_COLOR_PAIR(11))
PINK = lambda s: (CCHAR(s), PD_COLOR_PAIR(12))
LIGHT_MAGENTA = lambda s: (CCHAR(s), PD_COLOR_PAIR(13))
LIGHT_YELLOW = lambda s: (CCHAR(s), PD_COLOR_PAIR(14))
CLEAR_WHITE = lambda s: (CCHAR(s), PD_COLOR_PAIR(15))


def init_pairs():
    for n in range(16):
        init_pair(n, n, BG_COLOR)
