"""Tar Heels exercise redux as a structured program."""

__author__ = "730384155"


from random import choice
i: int = 0
j: int = 1


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(Ramsees: int) -> str:
    """UNC."""
    s: str = ""
    if Ramsees % 2 == 0:
        if Ramsees % 7 == 0:
            s += "TAR HEELS"
        else:
            s += "TAR"
    elif Ramsees % 7 == 0:
        s += "HEELS"
    else:
        s += "CAROLINA"
    return s


if __name__ == "__main__":
    main()