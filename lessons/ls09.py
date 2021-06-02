"""An example function definition"""

c: int = int(input("Enter a value for a: "))
d: int = int(input("Enter a value for b: "))

def my_max(a: int, b: int) -> int:
    if a > b:
        return a
    elif a == b:
        return a and b
    else:
        return b

if __name__ == '__main__':
    result: int = my_max(c,d)
    print(result)
