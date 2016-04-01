from data import objects
from data import monsters
from Classes.HelperClasses import CharParam
from Classes.GameObject import *


class Hero(GameObject):
    def __init__(self, char, field):
        GameObject.__init__(self, char, field)

        self.name = "Knight"
        self.keys = CharParam(value=0, max_value=4, unicode="⚷", empty_unicode="◯")
        self.lives = CharParam(value=3, max_value=4, unicode="♥", empty_unicode="♡")

    def events(self, key):
        if key == 'a':
            dir = LEFT
        elif key == 'd':
            dir = RIGHT
        elif key == 'w':
            dir = UP
        elif key == 's':
            dir = DOWN
        else:
            self.field[self.pos.y][self.pos.x] = self.char
            return
        if self.check_interact(dir):
            self.to_interact(dir)
        elif self.check_barrier(dir):
            self.move(dir)

    def to_interact(self, dir):
        """
        Взаимодейсвуем с интерактивным объектом
        """
        target_x, target_y = self.directions[dir]()
        for obj in objects.GAME_OBJECTS:
            if obj.get("char") == self.field[target_y][target_x]:
                obj["do"](self, target_x, target_y)
        # for monster in monsters.GAME_MONSTERS:
        #     if monster.get("char") == self.field[target_y][target_x]:
        #         monster

    def check_interact(self, dir):
        """
        Проверяем наличие интерактивного объекта
        """
        target_x, target_y = self.directions[dir]()
        if self.field[target_y][target_x] in objects.INTERACTIVE_OBJECTS:
            return True
        else:
            return False

    def get_damage(self, value):
        self.lives -= value

    def fight(self, target):
        target.die()

    def check_barrier(self, dir):
        """
        Проверяем проходимость тайла по направлению(dir)
        """
        # from data import objects
        # from data import monsters

        target_x, target_y = self.directions[dir]()
        if self.field[target_y][target_x] in objects.IMPASSABLE_OBJECTS:
            return False
        else:
            return True
