"""Tracing some while loops"""

__author__ = "730384155(Davis Atwell)"

# Globals
i: int = 1
j: int = 0 # j is usually defined in the python world as "i - 1"
s: str = "" # empty string to have values added to it
while i < 4:
    j = i + j
    s = s + str(i) + str(j)
    i += 1 # Used to prevent infinite loop and check more tests
print(s)

# While loop Ex. # 2
# def function():
i: int = 0
comp: str = "COMP"
while i < 5:
    comp += str(i)
    if (i % 2 == 0):
        i += 2
    i += 1
print(comp)
#function()