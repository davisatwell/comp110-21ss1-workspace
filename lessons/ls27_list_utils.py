"""Writing and Testing a max Function."""


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