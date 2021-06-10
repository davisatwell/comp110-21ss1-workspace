"""A simply function to sum up a list."""

test_list: list[int] = [1, 2, 3]

def sum_algo(xs: list[int]) -> int:
    """Summation of input list is returned."""
    total: int = 0
    # i: int = 0
    # while i < len(xs):
    #     total += xs[i]
    #     i += 1
    for element in xs:
        total += element
    return total

# Now with use of for...in alone

def sum_algo1(xs: list[int]) -> int:
    """Summation of input list is returned."""
    total: int = 0
    for element in xs:
        total += element
    return total

print(sum_algo1(test_list))  # Returns '6'

# def sum_two_lists(xs: list[int], ys: list[int]) -> int:
#     """Summation of two lists"""
#     new_list: list[int] = xs + ys
#     total: int = 0
#     for e in new_list:
#         total += e
#     return total

# pp: list[int] = [1, 2, 3]
# pj: list[int] = [4, 5, 6]

# print(sum_two_lists(pp,pj))

def sum_two_list1(xs: list[int], ys: list[int]) -> list[int]:
    result: list[int] = []
    for i in range(len(xs)):
        result.append(xs[i] + ys[i])
    return result

arg_1: list[int] = [1, 2, 3]
arg_2: list[int] = [4, 5, 6]

print(sum_two_list1(arg_1, arg_2)) # Output is [5, 7, 9]


