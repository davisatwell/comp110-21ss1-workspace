"""A function to abbreviate strings."""

__author__ = "730384155"


x: str = input("Enter desired words: ")
s1: str = ""


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print(abbreviate(x))


def abbreviate(char: str) -> str:
    """Abbreviate any given string."""
    i: int = 0
    global s1
    user_input: str = x
    while i < len(user_input):
        if user_input[i].isupper():
            s1 += user_input[i]
        i += 1
    return f"The abbreviation is \"{s1}\"."


if __name__ == "__main__":
    main()
