"""Word and character counting module"""


def count_words(contents: str) -> int:
    """Return the number of whitespace-separated words in the given text."""
    words = contents.split()
    return len(words)


def char_count(contents: str) -> dict[str, int]:
    """Returns the number of times each character appears in the string."""
    lower = contents.lower()
    characters = {}
    for char in lower:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters


def sort_on(item: dict) -> list:
    """Takes a dictionary and returns the value keys"""
    return item["num"]


def sort_char(provide_dict: dict) -> list[dict]:
    """Takes a dictionary and returns a sorted list of dictionaries"""
    list_dict = []
    for letter in provide_dict:
        letters = {}
        value = provide_dict[letter]
        letters["char"] = letter
        letters["num"] = value
        list_dict.append(letters)
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict


# if __name__ == "__main__":
#     test_chars = {"a": 10, "b": 3, "c": 7}
#     result = sort_char(test_chars)

#     print(result)
