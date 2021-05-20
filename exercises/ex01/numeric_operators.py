"""Demonstrating **, /, //, and %."""

__author__: str = "730384155"

left: str = input("Left-hand side:")
right: str = input("Right-hand side:")
sol1 = int(left) ** int(right)
sol2 = int(left) / int(right)
sol3 = int(left) // int(right)
sol4 = int(left) % int(right)
print(str(left), "**", str(right), "is", str(sol1))
print(str(left), "/", str(right), "is", str(sol2))
print(str(left), "//", str(right), "is", str(sol3))
print(str(left), "%", str(right), "is", str(sol4))
