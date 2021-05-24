"""An exercise in remainders and boolean logic."""

__author__ = "730384155"


num: int = int(input("Chose a number: "))

if (num % 2) == 0:
    if num % 7 == 0:
        print("TAR HEELS")
    else:
        print("TAR")
else:
    if num % 7 == 0:
        print("HEELS")
    else:
        print("CAROLINA")