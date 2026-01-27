def get_book_text(filepath: str) -> str:
    """Return the full text of the book at the given filepath."""
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents


def count_words(contents):
    words = contents.split()
    return len(words)


def main():
    filepath = "books/frankenstein.txt"
    contents = get_book_text(filepath)
    num_words = count_words(contents)
    print(f"Found {num_words} total words")


main()
