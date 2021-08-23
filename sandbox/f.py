# def tree(s: str, i: int) -> str:
#     if i >= len(s) - 1:
#         return s[len(s) - 1]
#     else:
#         print("New Frame")
#         a = tree(s, i + 1)
#         b = s[i]
#         c = tree(s, i + 1)
#         return a + b + c

# tree("hpy", 1)


# def f(x: float) -> int:
#     return int(x)

# def g(x: str) -> float:
#     return float(x)

# y = f(g("3.14"))

def main() -> None:
    n: int = 21
    print(april(fool(n - 19) + 1))

def fool(n: int) -> int:
    if n % 2 == 0:
        return 0
    elif n >= 50:
        return 1
    elif n < 20:
        return 2
    else:
        return 3

def april(x: int) -> int:
    h: int = -110
    while x >= 0 or h < 0:
        h *= -1
        x -= 1
    return x + h

if __name__ == "__main__":
    main()
