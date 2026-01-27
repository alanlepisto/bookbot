"""Word couting module"""


def count_words(contents: str) -> int:
    """Return the number of whitespace-separated words in the given text."""
    words = contents.split()
    return len(words)
