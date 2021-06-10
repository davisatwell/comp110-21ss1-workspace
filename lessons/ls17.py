"""For in Loop Practice"""

s: str = "Davis Atwell"
i: int = 0
# while i < len(s):
#     """Prints each character of the globally defined string 's'."""
#     print(s[i])
#     i += 1

# The above process can be done much easier with a for...in loop

for char in s:  # Will run for each character in the str collection 's' until the collection has completely been looped through
    print(char)
