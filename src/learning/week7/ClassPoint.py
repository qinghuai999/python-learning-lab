"""
File: ClassPoint.py
Author: Shiqi(Kiki) Su
Date: 2025-09-18 12:23
Description: Processing two points
"""
from __future__ import annotations
import math

EPSILON = 1e-5


class Point(object):
    """A 2D point in the cartesian plane"""

    def __init__(self, x: float, y: float) -> None:
        """
        Construct a 2D point object.

        Parameters:
            x: x coordinate in the 2D cartesian plane
            y: y coordinate in the 2D cartesian plane
        """

        self._x = x
        self._y = y

    def __repr__(self):
        return 'Point({}, {})'.format(self._x, self._y)

    def dist_to_point(self, other: Point) -> float:
        """
        Calculate the Euclidean distance between this point and another point.

        Args:
            other (Point): The other point to which the distance will be
            calculated.

        Returns:
            float: The Euclidean distance between self and others.

        Examples:
          >>> x, y = Point(0, 0), Point(3, 4)
          >>> x.dist_to_point(y)
          5
        """
        dx = self._x - other._x
        dy = self._y - other._y
        return math.sqrt(dx ** 2 + dy ** 2)

    def is_near(self, other: Point) -> bool:
        """
        Determine whether this point is close to another point.
        Two points are considered close if their Euclidean distance is less
        than the global constant EPSILON.
        Args:
            other (Point): The other point to compare against.

        Returns:
            bool: True if the distance is less than EPSILON, otherwise False.

        Examples:
          >>> x, y = Point(0, 0), Point(3, 4)
          >>> x.is_near(y)
          False
          >>> x, y = Point(0, 0), Point(10**-6, 10**-6)
          True
        """
        return self.dist_to_point(other) < EPSILON

    def add_point(self, other: Point) -> None:
        """
        Add the coordinates of another point to this point.

        The x- and y-coordinates of 'other' are added to the x- and
        y-coordinates of this point. This method modifies the current point
        in place.

        Args:
            other (Point): The point, whose coordinates will be added to
            this point.

        Returns:
            None

        Examples:
          >>> x, y = Point(1, 2), Point(3, 4)
          >>> x.add_point(y)
          >>> x
          Point(4, 6)
        """
        self._x += other._x
        self._y += other._y
