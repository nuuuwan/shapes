from shapes.core.Point import Point


class BBox:
    def __init__(self, min_point: Point, max_point: Point) -> None:
        self.min_point = min_point
        self.max_point = max_point
