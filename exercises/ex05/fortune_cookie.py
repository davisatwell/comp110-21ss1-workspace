"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730384155"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune)
    print("Now, go spread positive vibes!")

i: int = 0
j: int = 1
num: int = randint(0,2)
def fortune_cookie()-> str: 
    s: str = ""
    if num == 0:
        s += "You will find the love of your life soon"
    elif num == 1:
        s += "You will become rich soon!"
    else:
        s += "You will be given UNC basketball tickets next season!"
    return s
fortune = fortune_cookie()

# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
        main()