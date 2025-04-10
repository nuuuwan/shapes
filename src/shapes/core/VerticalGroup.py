from functools import cached_property

from utils import _

from shapes.core.Group import Group
from shapes.core.Point import Point
from shapes.core.Size import Size


class VerticalGroup(Group):

    def render(self, origin: Point):
        x_offset = 0
        y_offset = -self.size.height / 2

        rendered_child_list = []
        for child in self.children:
            y_offset += child.size.height / 2
            rendered_child = child.render(
                Point(origin.x + x_offset, origin.y + y_offset)
            )
            rendered_child_list.append(rendered_child)
            y_offset += child.size.height / 2

        return _("g", rendered_child_list)

    @cached_property
    def size(self):
        width = max(child.size.width for child in self.children)
        height = sum(child.size.height for child in self.children)
        return Size(width, height)
