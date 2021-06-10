"""Pet Breed Updating"""

breed: str = ""


def a() -> None:
    """Procedure to update breed."""
    global breed
    breed = "pug"
    return None


def b(s: str) -> str:
    """Function to update breed."""
    s += "!!!!"
    return s


def main() -> None:
    """Entrypoint of a program."""
    global breed
    a()
    breed = b(breed)
    print(breed)
    return None


if __name__ == "__main__":
    main()