"""Simple example of union types."""

from typing import Union

def add_or_concat(x: Union [str, int]) -> Union[str, int]:
    """Add or concatenate 10 depending on type."""
    if isinstance(x, int):
        return x + 10
    else:
        return x + "10"

print(add_or_concat(5)) # Output is: '15'

print(add_or_concat("5")) # Output is: '510'

print(add_or_concat("Ben ")) # Output is: 'Ben 10'