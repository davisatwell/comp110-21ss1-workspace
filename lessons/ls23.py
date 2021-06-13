"""Future"""
# this line allows you to use a [class_name] object within methods in said [class_name]
from __future__ import annotations, unicode_literals

class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        x: float = self.x + other.x
        y: float = self.y + other.y


def main() -> None:
        a: Point = Point(1.0, 2.0)
        b: Point = Point(3.0, 4.0)
        c: Point = a.add(b)