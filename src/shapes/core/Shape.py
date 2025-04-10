from shapes.core.Size import Size


class Shape:
    def __init__(self, size: Size, style: dict):
        self.size = size
        self.style = style
