"""Simple script to read Frankenstein and print its total word count."""

import sys
from stats import count_words
from stats import char_count
from stats import sort_char


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
    num_char = char_count(contents)
    sorted_report = sort_char(num_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for let in sorted_report:
        # print(f"let {let}")
        remove = let["char"]
        # print(remove)
        if remove.isalpha() == True:
            removed = remove
            print(f"{removed}: {let["num"]}")
    print("============= END ===============")


main()
