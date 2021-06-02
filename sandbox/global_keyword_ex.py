"""Example of using global keyword."""

x: int = 10

def x_update() -> int:
    global x
    x += 1
    return x #returns the value of x as 11 now

print(x_update())