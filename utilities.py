import os
import time

if os.name == 'nt':
    import msvcrt
else:
    import sys
    import termios
    import tty


def cls():
    """
    Очищаем консоль
    """
    os.system(['clear', 'cls'][os.name == 'nt'])

# def cls_fast(template):
#     ind =


class Clock:
    def __init__(self):
        self.start = time.time()

    def tick(self, fps):
        end = time.time()
        cur_dt = end - self.start
        need_dt = 1000/fps
        if cur_dt < need_dt:
            time.sleep((need_dt - cur_dt)/1000)
            self.start = time.time()


def getchar(locked=True):
    """
    Returns a single character from standard input
    """
    # Windows
    if os.name == 'nt':
        if not locked:
            if msvcrt.kbhit():
                try:
                    char = msvcrt.getch().decode("utf-8")
                except UnicodeDecodeError:
                    char = ''
                return char
        else:
            try:
                char = msvcrt.getch().decode("utf-8")
            except UnicodeDecodeError:
                char = ''
            return char

    # Posix (Linux, OS X)
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


# def animation():
#     level = LEVELS[LEVEL]
#     char_temp = None
#     for anim in animations_list[:]:
#         for frame in anim["frames"]:
#             if char_temp is None:
#                 char_temp = level[anim["pos"][1]][anim["pos"][0]]
#             level[anim["pos"][1]][anim["pos"][0]] = frame
#             cls()
#             render(level, status_bar.render())
#             # time.sleep(anim["speed"])
#         level[anim["pos"][1]][anim["pos"][0]] = char_temp
#         cls()
#         render(level, status_bar.render())
#         char_temp = None
#         animations_list.remove(anim)