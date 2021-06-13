"""Example of object oriented programming concepts."""

# class name
class Point:
    """Represents a 2D point."""

    # define attributes (related variables)
    x: float = 1.0
    y: float = 2.0

    # Define our own constructor
    def __init__(self, a: float, b: float):
        """Construct a point by giving a specific x and y."""
        # update our attributes to be assigned the value of the parameters
        self.x = a
        self.y = b
    
    def translate_x(self, dx: float) -> None:
        """Translate the point in the x direction."""
        # Mutate the object it is called on
        self.x += dx  # dx stands for 'delta x'
        return None
    
    def reset_y(self) -> None:
        """Return the current value of y and reset it."""
        result: float = self.y
        self.y = 0.0
        return result
    
# declare a new Point object, we need to call the constructor
a: Point = Point(30.0,40.0)

print(a) # Prints out where this defined data type is stored in memory
print(a.x) #'var_name.attribute' represents that attributes value in the created variable
print(a.y) # "      same explanation as above  (access attributes using the dot operator"
# you can also directly update attributes using the dot operator
a.x = 20.0

# Method call! We provide the specific object being used
# and the method name with arguments
a.translate_x(-6.0)


b: Point = Point(23.0, 69.0) # new table on heap

# You can assign a method call value to a var of the same return type
c: float = a.reset_y()
print(f"The value of C is {c}")
print(f"The value of a's Y coordinate has been reset to {a.y}")

# b.x = 2.0
# b.y = -1.0
print(b)
print(b.x,b.y)
# condense the code from 3 lines to one
# goes from...
"a: Point = Point()"
"a.x = 20.0"
"a.y = 21.0"
# to... (w use of constructor)
"a: Point = Point(20.0,21.0)"