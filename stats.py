"""Word and character counting module"""


def count_words(contents: str) -> int:
    """Return the number of whitespace-separated words in the given text."""
    words = contents.split()
    return len(words)


def char_count(contents: str) -> dict:
    """Returns the number of times each character appears in the string."""
    lower = contents.lower()
    characters = {}
    for char in lower:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters
