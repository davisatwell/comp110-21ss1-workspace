"""Looping with subscript notation with the use of incrimenting."""

def sub_notation(word: str) -> str:
    i = 0
    s = ""
    while i < len(word):
        s += word[i]
        i += 1
    return s

print(sub_notation("Hello, world."))