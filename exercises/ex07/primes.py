"""An exercise with functions and lists."""

__author__ = "730384155"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print(is_prime(9))

def is_prime(num: int) -> bool:
    """Testing if a number is prime."""
    i: int = 2
    if num < 2:
        return False
    while num > i:
        if num % i == 0 and i != num:
            print("not prime")
            return False
        i += 1    
    return True
    

# def is_prime(num: int) -> bool:
#  """Testing if a number is prime."""
#  i: int = 0
#  j: int = 1
#  test_var = num % j
#  l: range = range(0, num + 1)
#  if test_var * l[i] == int:
#     return False
#  elif num <= 1:
#     return False
#  i += 1
#  j += 1
#  if i > num:
#         return True





# TODO 2: Define the list_primes function, and its logic, here.


if __name__ == "__main__":
    main()