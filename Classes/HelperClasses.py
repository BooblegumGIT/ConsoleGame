class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __repr__(self):
        return "pos({}, {})".format(self.x, self.y)

    def as_point(self):
        return self.x, self.y


class CharParam:
    def __init__(self, value=0, max_value=0, unicode=" ", empty_unicode=" "):
        self.value = value
        self.max_value = max_value
        self.unicode = unicode
        self.empty_unicode = empty_unicode

    def __str__(self):
        return "{}{}".format(self.unicode * self.value, self.empty_unicode * (self.max_value - self.value))

    def __format__(self, format_spec):
        return str.__format__(self.__str__(), format_spec)

    def __add__(self, other):
        self.value = self.max_value if self.value + other > self.max_value else self.value + other
        return self

    def __sub__(self, other):
        self.value = 0 if self.value - other < 0 else self.value - other
        return self

    def __bool__(self):
        return bool(self.value)