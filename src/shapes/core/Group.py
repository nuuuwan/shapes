from functools import cached_property

from utils import _

from shapes.core.Point import Point
from shapes.core.Size import Size


class Group:
    def __init__(self, *children):
        self.children = children

    def render(self, origin: Point):

        rendered_child_list = []
        for child in self.children:
            rendered_child = child.render(origin)
            rendered_child_list.append(rendered_child)

        return _("g", rendered_child_list)

    @cached_property
    def size(self):
        width = max(child.size.width for child in self.children)
        height = max(child.size.height for child in self.children)
        return Size(width, height)
