"""This file is an example."""
from random import randint

x: int = 13   #globals vars on lines one and two
y: int = 49

def sum(a: int, b: int) -> int:
    w: int = a + b   # local variable that only exists inside of the defined function named "sum"

#sum(x,y)

movie: int = randint(1,8)
print(movie)

