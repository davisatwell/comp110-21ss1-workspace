"""Exploring command line arguments."""
("Allows us to create a file as a list of its arguments[probably useful for notebooks]")
# Gives us access to the arguments our program begins with
import sys

# argv is just the list of arguments our program is begun with
# by default, when you begin a program from the command line
# the first argument is the file you are trying to run
print(sys.argv)

# sys.argv has type of list[str]

args: list[str] = sys.argv
print(args)


# IN REPL (Proof sys.argv has typ list[str]):

# davisatwell@daviss-Air comp110-21ss1-workspace % python -m lessons.ls26_cli_args one two three four five
# ['/Users/davisatwell/comp110-21ss1-workspace/lessons/ls26_cli_args.py', 'one', 'two', 'three', 'four', 'five']

# Input for next 3 lines of code:
# davisatwell@daviss-Air comp110-21ss1-workspace % python -m lessons.ls26_cli_args 29 + 45  
# >>>['/Users/davisatwell/comp110-21ss1-workspace/lessons/ls26_cli_args.py', '29', '+', '45']

print(len(args))
print(args[0])
print(args[1])

# Output of lines 25, 26, and 27:

# 4
# /Users/davisatwell/comp110-21ss1-workspace/lessons/ls26_cli_args.py
# 29


# spaces between words determine the seperation of arguments
# can put quotes to have a multiple word argument

#Specify the Problem we want to solve
# run our program as a module with two command line arguments
#1. name of the file we'd like to search
#2. search term we are looking for
# print out all the lines containing the search term and
# give the total number of matches


def read_args() -> dict[str, str]:
    """Check for valid CLI arguments and return them in a dictionary."""
    


def main() -> None:
    """Entrypoint."""


    if __name__ == "__main__":
    main()