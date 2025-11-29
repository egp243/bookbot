def get_book_text(path):
    """
    Reads the file at the given path and returns the entire text as a string.
    """
    with open(path) as book:
        book_contents = book.read()
        return book_contents


def word_counter(text):
    """
    Takes a string of text and returns the total number of words.
    """
    count_words = text.split()
    return len(count_words)


def char_counter(text):
    """
    Counts how many times each character appears in the text.
    Converts all characters to lowercase to ensure 'A' and 'a' are counted together.
    Returns a dictionary like {'a': 5, 'b': 2}.
    """
    char_dict = {}

    for c in text:
        lower_c = c.lower()
        if lower_c in char_dict:
            char_dict[lower_c] += 1
        else:
            char_dict[lower_c] = 1
    return char_dict


def sort_on(item):
    """
    Helper function used by the .sort() method.
    Tells Python to sort based on the "num" key.
    """
    return item["num"]


def sort_characters(char_dict):
    """
    Takes the dictionary of character counts and converts it into a 
    sorted list of dictionaries, ordered from highest count to lowest.
    Example: [{'char': 'e', 'num': 100}, {'char': 't', 'num': 80}]
    """
    sorted_char = []

    for char, cnt in char_dict.items():
        sorted_char.append({"char": char, "num": cnt})
    
    # Sort the list in reverse order (highest to lowest) using the 'num' key
    sorted_char.sort(reverse=True, key=sort_on)
    return sorted_char