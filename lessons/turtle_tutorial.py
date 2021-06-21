from typing import Union
from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
print(leo.position()) # Starting position of Turtle object named "leo"

# In order to move the turtle to a new drawing location:
leo.penup() #OR leo.up to pull pen off page (aka Turtle object "leo" in this scenario)
leo.goto(45, 60)
leo.pendown() # OR leo.down to put the pen back on the page

i: int = 0
while (i < 3): # GF for repeating a move: (<counter_variable> < <number_of_times>)
    leo.forward(300)
    leo.right(120)
    i += 1


# class Leo:
#     angle: Union[int, float]
#     leo: Turtle = Turtle()
    
done() # the done() function must come after all of the turle functions that you want to see on the window

# def turtle(turtle: Turtle, distance: Union[int, float], angle: Union[int, float]) -> Turtle:
#     """Function that can be used to draw with Turtle."""
