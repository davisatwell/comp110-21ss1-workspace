"""Relative reassignment."""
# Global Vars
a: int = 3
b: str = "<"
iterations: int = 0

b += str(a)
print(b)
b += str(a)
print(b)
b += str(a)
print(b)

# Using Loop
while iterations < 3:
    b += str(a)
    print(b)
    iterations += 1

print("loop done!")