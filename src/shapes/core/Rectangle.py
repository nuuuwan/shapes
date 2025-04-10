from utils import _

from shapes.core.Point import Point
from shapes.core.Shape import Shape


class Rectangle(Shape):
    def render(self, origin: Point) -> None:
        return _(
            "rect",
            None,
            dict(
                x=origin.x - self.size.width / 2,
                y=origin.y - self.size.height / 2,
                width=self.size.width,
                height=self.size.height,
                fill=self.style["fill"],
            ),
        )
