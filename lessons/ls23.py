"""Operator Overloading in class __methods__"""
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
        return Point(x,y)

    def __add__(self, other: Point) -> Point: #__add__ has the same def as add, dunderscores make it an operator overloading scenario that allows "+" to invoke arithmetic addition
        print("Inside the Special method for add oo!!")
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x,y)

    def __mul__(self, other: Point) -> Point:
        """Multiplication overloading."""
        x: float = self.x * other.x
        y: float = self.y * other.y
        return Point(x,y)

    def __getitem__(self, index: int) -> float:
        # if index == 0:
        #     return self.x
        # else:
        #     return self.y
        # more precisely...
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError

    def __gt__(self, other: Point) -> bool:
        """Comparing X attributes of self and other."""
        return self.x > other.x

    def __repr__(self) -> str:
        """Automagically invoke Point object to be printed."""
        representation: str = f"The point values of this object are {self.x} and {self.y}"
        return representation        
    

def main() -> None:
        """Entrypoint of program."""
        a: Point = Point(1.0, 2.0)
        b: Point = Point(3.0, 4.0)
        c: Point = a.add(b) # [Output] Point C 4.0 6.0
        print(f"Point C: {c.x, c.y}")
        d: Point = a + b # same as a.__add__(b)
        f: Point = a.__add__(b)
        e: Point = a * b # can use "*" with type Point now because of creating a __mul__ operator overload
        g: Point = a.__mul__(b) # same value as the line above, just displayed at a lower level view of code
        print(f"Point G: {g.x}, {g.y}")
        print(f"Point F: {f.x}, {f.y}")
        print(f"Point D: {d.x}, {d.y}")
        print(a[0]) # prints self.x
        print(a[1]) # prints self.y, is like saying...
        print(f"The value at A's index of 1 is: {a.__getitem__(1)}")
        # __getitem__ can be invoked by [i] or class_object.__getitem__(index: int)
        # print(a[100]) # raises an IndexError
        print("__gt__ bool result:")
        print(a.x > b.x)
        print("a object info: ")
        print(a) # produces the str value of "The point values of this object are 1.0 and 2.0"

if __name__ == '__main__':
    main()

