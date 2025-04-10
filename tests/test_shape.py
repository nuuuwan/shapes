import os
import unittest

from shapes import (Canvas, Group, HorizontalGroup, Rectangle, RegularPolygon,
                    Size, VerticalGroup)


class TestCase(unittest.TestCase):

    def test_rect(self):

        hexagon = Group(
            RegularPolygon(Size(100, 100), dict(fill="#c80"), n_sides=6),
            RegularPolygon(Size(80, 80), dict(fill="#fff"), n_sides=6),
        )
        lid_rect = Rectangle(
            Size(300, 10),
            dict(fill="#a60"),
        )
        foreground = VerticalGroup(
            lid_rect,
            HorizontalGroup(hexagon, hexagon, hexagon),
            lid_rect,
        )
        background_rect = Rectangle(
            Size(350, 100),
            dict(fill="#fff"),
        )

        canvas = Canvas(
            Group(
                background_rect,
                foreground,
            )
        )

        svg_path = os.path.join("tests", "output", "test_rect.svg")
        canvas.write(svg_path)
