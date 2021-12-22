"""A program to hype you up."""
import random
import sys

def main(args: list[str]) -> None:
    repeats: int = int(args[1])
    while repeats > 0:
        random_number: int = int(random.random()*3)
        if random_number == 0:
            print("You are awesome!")
        else:
            if random_number == 1:
                print("You're the best!!!")
            else:
                print("Keep up the great work!!!")
        repeats -= 1

# Lines 5-16 and Lines 20-21 have now allowed us to control how 
# many times we want the while loop on line 7 to repeat from 
# the Command Line

if __name__=="__main__":
    main(sys.argv)