"""A problematic function!"""

def f(a: int) -> str:
    if a >= 2:
        return "Greater than or eq to 2"
    else:
        if a < 2:
            return "less than"
        else:
            return "you'll never actually get here"

# Even though the last else statement (line 9) is useless, this statement leaves no open ended possibility of a condition not being made in our statements/tests.

