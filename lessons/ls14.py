"""Named constants and f-strings."""

INTEREST_RATE: float = 0.009

def compound(current_balance: float) -> float: # argument is a float because money is tracked in decimal values.
    # print("The interest rate is", str(INTEREST_RATE))
    print(f"The interest rate is {INTEREST_RATE}") # Same functional use as line 6 code but simplified through the use of F-Strings
    return current_balance + (current_balance * INTEREST_RATE)

compound(10.0)

# line 7- F-String
# line 3- Named Constant