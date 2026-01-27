"""Simple script to read Frankenstein and print its total word count."""

from stats import count_words


def get_book_text(filepath: str) -> str:
    """Return the full text of the book at the given filepath."""
    with open(filepath, encoding="utf-8") as file:
        file_contents = file.read()
    return file_contents


def main() -> None:
    """Read the book, count its words, and print the total."""
    filepath = "books/frankenstein.txt"
    contents = get_book_text(filepath)
    num_words = count_words(contents)
    print(f"Found {num_words} total words")


main()
