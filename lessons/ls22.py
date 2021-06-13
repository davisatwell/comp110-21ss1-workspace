"""Defining a simple class."""

class Person:
    """Representation of a person."""
    name: str
    age: int

    def __init__(self, name: str, age: int):
        """Initialize our attributes."""
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        """Provides a str representation of a Person object."""
        representation: str = f"{self.name} is a person who is {self.age} year old."
        return representation

davis: Person = Person("davis", 18)
print(f"Name: {davis.name}")
print(f"Age: {davis.age}")

# after the use of __repr__ (__repr__ tells the computer HOW to represent the return values of this class)
print("after the use of __repr__ , the comand print(davis) displays: ")
print(davis)
print("Instead of it printing the memory location address of the defined class.")



