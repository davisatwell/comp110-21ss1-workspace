"""Writing and Testing a max Function."""


# from _typeshed import StrPath


def max(xs: list[int]) -> int:
    """Finds the maximum value in a list."""
    if len(xs) == 0:
        raise ValueError("max function was given no args")
    curr_max: int = xs[0]
    if len(xs) == 1:
        curr_max = xs[0]
        return curr_max
    elif len(xs) > 1:
        for item in range(len(xs)):
            if xs[item] > curr_max:
                    curr_max = xs[item]
    return curr_max

def concat(a: list[int], b: list[int]) -> list[int]:
    """Combining two lists of int into one."""
    result: list[int] = []
    for elt in a:
        result.append(elt)
    for elt in b:
        result.append(elt)
    return result


def all(xs: list[int], needle: int) -> bool:
    """Return True if all elements are equal to the needle."""
    if len(xs) == 0: # Get rid of edge cases first (Pro Tip, makes writing rest of conditions easier)
        return False
    i: int = 0
    while i < len(xs):
        if xs[i] != needle:
            return False
        i += 1
    return True


def sub(a: list[int], start: int, end: int) -> list[int]:
    """Construction on a sub list based on input range."""
    if a == [] or start >= end:
        return []
    elif start < 0:
        start = 0
    elif end > len(a):
        end = len(a)
    result: list[int] = []
    for i in range(start, end):
        result.append(a[i])
    return result

# print(sub([1,2,3,4], 1, 3))
# lines 62-64 as a while loop
# i: int = start
# while i < end:
#     result.append(a[i])
#     i += 1

# def concat_2(a: list[int], b: list[int]) -> list[int]:
#     """Combining two lists of int into one using a while loop."""
#     result: list[int] = []
#     i: int = 0
#     while i < len(a):
#         result.append(a[i])
#         i += 1
#     j: int = 0
#     while j < len(b):
#         result.append(b[i])
#         j += 1
#     return result