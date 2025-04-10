import os
from functools import cached_property

from utils import _

from shapes.core.BBox import BBox
from shapes.core.Point import Point
from shapes.core.Shape import Shape
from shapes.core.Size import Size


class Canvas:
    def __init__(self, *shapes: list[Shape]):
        self.shapes = shapes

    def write(self, svg_path: str) -> None:
        svg = _(
            "svg",
            [shape.render(Point(0, 0)) for shape in self.shapes],
            dict(viewBox=self.viewbox),
        )
        svg.store(svg_path)
        os.startfile(svg_path)

    @cached_property
    def bbox(self) -> Size:
        min_x, min_y = float("inf"), float("inf")
        max_x, max_y = float("-inf"), float("-inf")
        for shape in self.shapes:
            width, height = shape.size.width, shape.size.height
            min_x = min(min_x, -width / 2)
            min_y = min(min_y, -height / 2)
            max_x = max(max_x, +width / 2)
            max_y = max(max_y, +height / 2)
        return BBox(
            Point(min_x, min_y),
            Point(max_x, max_y),
        )

    @cached_property
    def viewbox(self) -> str:
        bbox = self.bbox
        return (
            f"{bbox.min_point.x} {bbox.min_point.y} "
            + f"{bbox.max_point.x - bbox.min_point.x} "
            + f"{bbox.max_point.y - bbox.min_point.y}"
        )
