from Classes.HelperClasses import Point

# const
LEFT = 4
RIGHT = 6
UP = 8
DOWN = 2


class GameObject:
    def __init__(self, char, field):
        self.char = char

        self.field = field
        self.temp_current_tile_char = " "

        self.directions = {LEFT: self.__get_pos((-1, 0)),
                           RIGHT: self.__get_pos((1, 0)),
                           UP: self.__get_pos((0, -1)),
                           DOWN: self.__get_pos((0, 1)),
        }
        self.pos = Point(*self.__find_pos())

    def __get_pos(self, d_pos):
        def wrapper():
            return self.pos.x + d_pos[0], self.pos.y + d_pos[1]
        return wrapper

    def event(self, event):
        pass

    def move(self, dir):
        target_x, target_y = self.directions[dir]()
        self.field[self.pos.y][self.pos.x] = self.temp_current_tile_char
        self.temp_current_tile_char = self.field[target_y][target_x]
        self.field[target_y][target_x] = self.char
        self.pos.x, self.pos.y = target_x, target_y

    def __find_pos(self):
        j = 0
        i = -1
        for line in self.field:
            try:
                i = line.index(self.char)
                break
            except ValueError:
                j += 1

        if i == -1:
            raise AttributeError("Monster not found")
        else:
            return i, j

    def check_barrier(self, dir):
        """
        Проверяем проходимость тайла по направлению(dir)
        """
        from data import objects
        from data import monsters

        target_x, target_y = self.directions[dir]()
        if self.field[target_y][target_x] in (objects.IMPASSABLE_OBJECTS + monsters.IMPASSABLE_OBJECTS):
            return False
        else:
            return True