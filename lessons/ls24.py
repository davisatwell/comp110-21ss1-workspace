"""Practice with Union."""

from __future__ import annotations
# line of code below allows you to use Union types in this file...
from typing import Union

# General Form of a Union:
var_0: Union[int, str, list, dict, float] # (etc. of data types in brackets)

# saying "x can either be type str OR type int"
x: Union[str, int] 

# isinstance() # a built-in function for checking the type of an expression

# General Form of isinstance(): isinstance(expression, className) -> bool:

# Examples:
isinstance(1, int) # -> returns True
isinstance(1, str) # -> returns False

y: bool = isinstance(69, int)
print(f"y is assigned the bool value of: {y}")