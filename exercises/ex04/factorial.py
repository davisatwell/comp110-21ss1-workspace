"""An exercise in computing the factorial of an int."""

__author__ = "730384155"

user_input: int = int(input("Pick a number to factorial: "))

i: int = 1
factorial: int = 1

while i <= user_input:
    factorial *= i
    i += 1    
else:
    print("Factorial is:", (str(factorial)))