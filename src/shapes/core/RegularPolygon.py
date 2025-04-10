import math

from utils import _

from shapes.core.Point import Point
from shapes.core.Shape import Shape
from shapes.core.Size import Size


class RegularPolygon(Shape):
    def __init__(self, size: Size, style: dict, n_sides: int):
        super().__init__(size, style)
        self.n_sides = n_sides

    def render(self, origin: Point) -> None:
        points = []
        for i in range(self.n_sides):
            angle = (2 * math.pi * i) / self.n_sides
            x = origin.x + self.size.width * math.cos(angle) / 1.9
            y = origin.y + self.size.height * math.sin(angle) / 1.7
            points.append((x, y))
        points_str = " ".join([f"{x},{y}" for x, y in points])
        return _(
            "polygon",
            None,
            dict(
                points=points_str,
                fill=self.style["fill"],
            ),
        )
