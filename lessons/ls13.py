"""Looping over a string."""

def string_indexing(word: str) -> str:
    """Get every other character of a word!"""
    i: int = 0
    new_word: str = ""
    while i < len(word):
        new_word += word[i]
        i += 2  # incrimenting the index by two instead of the usual one
    return new_word


print(string_indexing("boat"))