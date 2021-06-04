"""Random Shit."""

"""Problematic Function."""

def f(a: int) -> str:
    if a >= 2:
        return "Greater than or equal to 2"
    else:
        if a < 2: #remove this line of code to get rid of errors
            return "less than"
        #computer believes an else statement belongs here to make sure a condition is met, but our human logic knows that a condition will be met in above lines, but computer does not know this.
# Computer thinks that nothing will be returned if neither of these conditions are met.
# BUT the first two conditions will always be met, but because of how the body block is laid out,
# The computer interpreted this as "open ended".

