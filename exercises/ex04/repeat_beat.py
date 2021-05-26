"""Repeating a beat in a loop."""

__author__ = "730384155"


beat: str = input("What beat do you want to repeat?")
iteration: int = int(input("How many times do you want to repeat it?"))
i: int = 1
j: int = 0
s: str = ""
if iteration <= 0:
    print("No beat...")
else:
    while iteration > i:
        s += beat + " "
        iteration -= 1
    if iteration == i:
        s += beat
    print(s)
