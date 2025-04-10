from functools import cached_property

from utils import _

from shapes.core.Group import Group
from shapes.core.Point import Point
from shapes.core.Size import Size


class HorizontalGroup(Group):

    def render(self, origin: Point):
        x_offset = -self.size.width / 2
        y_offset = 0
        rendered_child_list = []
        for child in self.children:
            x_offset += child.size.width / 2
            rendered_child = child.render(
                Point(origin.x + x_offset, origin.y + y_offset)
            )
            rendered_child_list.append(rendered_child)
            x_offset += child.size.width / 2

        return _("g", rendered_child_list)

    @cached_property
    def size(self):
        width = sum(child.size.width for child in self.children)
        height = max(child.size.height for child in self.children)
        return Size(width, height)
