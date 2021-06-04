"""A function to abbreviate strings."""

__author__ = "730384155"

x: str = input("Enter desired words: ")
s: str = ""

def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print(f"The abbreviation is \"{abbreviate(x)}\"")

def abbreviate(char: str) -> str:
    i: int = 0
    global s
    user_input: str = x
    if user_input.isupper():
        return user_input
    else:
        while i < len(user_input):
            if user_input[i].isupper():
                s += user_input[i]
            i += 1
        return s

if __name__ == "__main__":
    main()
