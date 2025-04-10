from shapes.core.Size import Size


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other: Size):
        return Point(self.x + other.width, self.y + other.height)
