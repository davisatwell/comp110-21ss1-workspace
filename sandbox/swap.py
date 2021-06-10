"""Swap"""

def swap(xs: list, i: int, j: int) -> None:
    temp: int = xs[i]
    xs[i] =xs[j]
    xs[j] = temp
    return None


nums: list[int] = [2, 3, 1, 4]
swap(nums, 2, 1)
swap(nums, 1, 0)
print(nums)
# Output is [1, 2, 3, 4]