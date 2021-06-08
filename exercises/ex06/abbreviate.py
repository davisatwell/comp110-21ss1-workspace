"""A function to abbreviate strings."""

__author__ = "730384155"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    x: str = input("Enter desired words: ")
    user_input: str = x
    print(f"The abbreviation is \"{abbreviate(user_input)}\".")


def abbreviate(char: str) -> str:
    """Abbreviate any given string."""
    s1: str = ""
    i: int = 0
    while i < len(char):
        if char[i].isupper():
            s1 += char[i]
        i += 1
    return s1


if __name__ == "__main__":
    main()
