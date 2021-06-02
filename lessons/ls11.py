def is_even(num: int) -> bool:
    """Evaluate if argument is even or not."""
    if num % 2 == 0:
        return True
    else:
        return False

users_int: int = int(input("Choose an int to test: "))
even_num_tester: bool = is_even(users_int)
print(even_num_tester)