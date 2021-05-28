"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730384155"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str: 
    """Fortune Cookie Message."""
    num: int = randint(0, 3)
    s: str = ""
    if num == 0:
        s += "You will find the love of your life soon!"
    elif num == 1:
        s += "You will become rich soon!"
    elif num == 2:
        s += "You will learn a life skill soon!"
    else:
        s += "You will be given UNC basketball tickets next season!"
    return s


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()