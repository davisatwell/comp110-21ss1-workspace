"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730384155"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


num: int = randint(1, 4)
print("Your fortune cookie says...")

if num <= 2:
    if num == 1:
        print("You will find the love of your life in the next year!")
    else:
        print("You will become wealthy very soon!")
else:
    if num == 3:
        print("Your family will suprise you with a gift soon!")
    else:
        print("You will get a new pet in the near future!")


print("Now, go spread positive vibes!")