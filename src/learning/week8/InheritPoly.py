"""
File: InheritPoly.py
Author: Shiqi(Kiki) Su
Date: 2025-09-28 12:39
Description:
"""

from __future__ import annotations

class Shape:
    """
    A representation of a shape.
    """

    def __init__(self, origin: tuple[int, int] = (0, 0)) -> None:
        """
        Construct a shape object
        Args:
            origin (tuple[int, int]): Origin of the shape
        """
        self.origin = origin

    def area(self) -> int:
        """
        Calculate the area of the shape.
        Returns:
            int: the total area
        """
        raise NotImplementedError

    def vertices(self) -> list[tuple[int, int]]:
        """
        Return the vertices of the shape in any order.
        """
        raise NotImplementedError

class Square(Shape):
    def __init__(self, side_length: int,
                 origin: tuple[int, int] = (0, 0)) -> None:
        super().__init__(origin=origin)
        self.side_length = side_length

    def area(self) -> int:
        return self.side_length * self.side_length

    def vertices(self) -> list[tuple[int, int]]:
        x, y = self.origin
        return [
            (x, y),
            (x, y + self.side_length),
            (x + self.side_length, y + self.side_length),
            (x + self.side_length, y),
        ]

def total_area(self, shapes: Square) -> list[Shape]:
    """
    Return the total area of the given list of shapes.
    Args:
        shapes (Square): The list of shapes to sum the area for.
    """
    area = 0.
    for shape in shapes:
        area += shape.area()
    return area

def outer_bounds(shapes: list[Shape]) -> tuple[
    tuple[int, int]]:
    """
        Return the outer bounds of the given list of shapes.

        Parameters:
            shapes: The list of shapes to return the outer bounds for.

        Note:
            The first element of the tuple is the top-left corner of a rectangle
            which could enclose every shape in the given list.
            The second element of the tuple is the bottom-right corner of that same
            rectangle.

            The top-left corner of the rectangle will be, at minimum, (0, 0).

        """
    vertices = []

    for shape in shapes:
        for vertex in shape.vertices():
            vertices.append(vertex)

    top_left_x = 0
    top_left_y = 0
    bottom_right_x = 0
    bottom_right_y = 0

    for x, y in vertices:
        if x < top_left_x:
            top_left_x = x
        elif x > bottom_right_x:
            bottom_right_x = x

        if y < top_left_y:
            top_left_y = y
        elif y > bottom_right_y:
            bottom_right_y = y

    return (top_left_x, top_left_y), (bottom_right_x, bottom_right_y)


class RightAngledTriangle(Shape):
    def __init__(self, vertices: list[tuple[int, int]]):
        super().__init__(origin=vertices[0])
        self._vertices = vertices

    def area(self) -> int:
        base = self._vertices[2][0] - self._vertices[0][0]  # x difference
        height = self._vertices[1][1] - self._vertices[0][1]  # y difference
        return base * height // 2

    def vertices(self) -> list[tuple[int, int]]:
        return self._vertices

class Rectangle(Shape):
    def __init__(self, width, height,
                 origin: tuple[int, int] = (0, 0)):
        super().__init__(origin=origin)
        self.width = width
        self.height = height

    def area(self) -> int:
        return  self.width * self.height

    def vertices(self) -> list[tuple[int, int]]:
        x, y = self.origin
        w, h = self.width, self.height
        return [
            (x, y),
            (x, y + h),
            (x + w, y + h),
            (x + w, y),
        ]







