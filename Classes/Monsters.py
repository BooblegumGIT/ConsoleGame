from Classes.GameObject import *
import random


class Monster(GameObject):
    def __init__(self, char, field, hero):
        GameObject.__init__(self, char, field)
        self.field[self.pos.y][self.pos.x] = " "
        self.hero = hero
        self.alive = True

    def come_back(self):
        """
        Побочный эффект MonsterCreator'а
        """
        self.field[self.pos.y][self.pos.x] = self.char
        pass

    def event(self, event):
        if self.check_distance() <= 0:
            self.attack()
        if not self.alive:
            return
        self.ai()
        if self.check_distance() == 1:
            self.poor_attack()
        elif self.check_distance() <= 0:
            self.attack()

    def ai(self):
        """
        Искуственный интелект монстра
        """
        # Опишите ИИ для каждого монстра в его классе
        pass

    def move(self, dir):
        GameObject.move(self, dir)

    def poor_attack(self):
        self.hero.get_damage(1)

    def attack(self):
        print(self, "attack")
        self.hero.fight(self)

    def check_distance(self):
        return abs(self.pos.x - self.hero.pos.x) + abs(self.pos.y - self.hero.pos.y)

    def die(self):
        print(self, "die")
        self.field[self.pos.y][self.pos.x] = "H"
        self.alive = False


class Snake(Monster):
    # def __init__(self, *args):
    #     Monster.__init__(self, *args)

    def ai(self):
        directions = [LEFT, RIGHT, UP, DOWN]
        select_dir = random.randint(0, len(directions)-1)
        dir = directions[select_dir]
        if self.check_barrier(dir):
            # pass
            self.move(dir)

    def __repr__(self):
        return "Snake {}".format(self.pos.as_point())


class Cat(Monster):
    pass


class Ghost(Monster):
    def ai(self):
        all_directions = [LEFT, RIGHT, UP, DOWN]
        directions = []

        if self.pos.x < self.hero.pos.x:
            directions.append(RIGHT)
        elif self.pos.x > self.hero.pos.y:
            directions.append(LEFT)
        if self.pos.y < self.hero.pos.y:
            directions.append(DOWN)
        elif self.pos.y > self.hero.pos.y:
            directions.append(UP)
        if random.randint(0, 100) < 25:  # 25% шанс выбрать произвольное направление
            remaining_directions = list(set(all_directions) - set(directions))
            directions.append(remaining_directions[random.randint(0, len(remaining_directions)-1)])
        select_dir = random.randint(0, len(directions)-1)
        dir = directions[select_dir]
        if self.check_perimetr(dir):
            # pass
            self.move(dir)

    def check_perimetr(self, dir):
        target_x, target_y = self.directions[dir]()
        if target_y > len(self.field)-1 or target_y < 0 or target_x > len(self.field[0])-1 or target_x < 0:
            return False
        return True


class MonsterCreator:
    def __init__(self, field, monsters, hero):
        field = field
        self.monster_objects = []
        for monster in monsters:
            char = monster["char"]
            while True:
                try:
                    self.monster_objects.append(monster["class"](char, field, hero))
                except AttributeError:
                    break
