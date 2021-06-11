"""An exercise with functions and lists."""

__author__ = "730384155"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print(is_prime(9))
    print(list_primes(10, 20))


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


def list_primes(a: int, b: int) -> list[int]:
    """List of prime numbers."""
    a_list = []
    while a <= b:
        a_list.append(a)
        a += 1
    # print(a_list)
    # z: int = 0
    prime_numbers: list[int] = []
    # while z < b:
    #     if is_prime(a_list[z]) == True:
    #         prime_numbers.append(a_list[z])
    #     z += 1
    # return prime_numbers
    for e in a_list:
        is_prime(e)
        if is_prime(e) is True:
            prime_numbers.append(e)
    return prime_numbers


if __name__ == "__main__":
    main()