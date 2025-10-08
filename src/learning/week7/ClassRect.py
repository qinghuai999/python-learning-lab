"""
File: ClassRect.py
Author: Shiqi(Kiki) Su
Date: 2025-09-18 14:44
Description:
"""
from __future__ import annotations


class Rectangle():
    def __init__(self, top_left: tuple[int, int],
                 width: int, height: int):
        self._x, self._y = top_left
        self._width = width
        self._height = height

    def get_bottom_right(self) -> tuple[int, int]:
        """
        Return the bottom right corner
        Returns:
            tuple[int, int]:
        """
        return self._x + self._width, self._y + self._height

    def move(self, new_corner: tuple[int, int]) -> None:
        """
        Move the rectangle that make the new_corner becomes the top-left
        corner. Width and height keep unchange.
        Args:
            new_corner (tuple[int, int]):

        Returns:
            None
        """
        self._x, self._y = new_corner

    def resize(self, new_width: int, new_height: int) -> None:
        self._width = new_width
        self._height = new_height

    def __str__(self) -> str:
        # bottom_right_corner = self._x + self._width, self._y + self._height
        return f"(({self._x}, {self._y}), {self.get_bottom_right()})"
