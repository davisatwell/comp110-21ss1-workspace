"""An example function definition"""

c: int = int(input("Enter a value for a: "))
d: int = int(input("Enter a value for b: "))

def my_max(a: int, b: int) -> int:
    """Returns the Largest Parameter."""
    if a > b:
        return a
    elif a == b:
        return a and b
    else:
        return b

# Use of main function - sets off other functions to go on adventure!
def main() -> None:
    """Entrypoint of a program."""
    result: int = my_max(c,d)
    print(result)

# main function
if __name__ == '__main__':
    main()
