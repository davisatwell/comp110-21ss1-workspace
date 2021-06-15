"""Examples of Vectorized Operations."""

from __future__ import annotations
from typing import Union

class StrArray:
    """Utility class for common string operations."""
    values: list[str]

    def __init__(self, v: list[str]):
        """Initializing a StrArray object."""
        self.values = v

    def __repr__(self) -> str:
        """Enable printing a var of class StrArray directly."""
        # representation: str = f"{self.values}"
        # return representation
        # OR... (to simplify lines of code)
        return f"StrArray({self.values})"
    
    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Enable + use with class StrArray and str objects."""
        new_values: list[str] = []
        if isinstance(rhs, StrArray): # Enters this block if trying to concatenate a StrArray object with a StrArray object
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                new_values.append(self.values[i] + rhs.values[i])
        elif isinstance(rhs, str): # Enters this block if trying to concatenate a StrArray object with a str object
            for item in self.values:
                new_values.append(item + rhs)
        return StrArray(new_values) # Must put StrArray in front of (new_values) because we want __add__ to return a StrArray object

s: StrArray = StrArray(["a", "b", "c"])
t: StrArray = StrArray(["d", "e", "f"])

print("OUTPUTS: ")
print(s) # Output is: StrArray(['a', 'b', 'c'])
print(t) # Output is: StrArray(['d', 'e', 'f'])
# print(f"StrArray({s + t})") # Output is: StrArray(['ad', 'be', 'cf'])
print(s + "!")
print(s + t)


