"""list utility functions."""

__author__ = "730384155"


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
    if len(xs) == 0:  # Get rid of edge cases first (Pro Tip, makes writing rest of conditions easier)
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
        end = (len(a) - 1)
    result: list[int] = []
    i: int = start
    while i < end:
        result.append(a[i])
        i += 1
    return result