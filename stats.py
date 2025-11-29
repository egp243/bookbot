def get_book_text(path):
    with open(path) as book:
        book_contents = book.read()
        return book_contents

def word_counter(text):
    count_words = text.split()
    return len(count_words)

def char_counter(text):
    char_dict = {}

    for c in text:
        lower_c = c.lower()
        if lower_c in char_dict:
            char_dict[lower_c] += 1
        else:
            char_dict[lower_c] = 1
    return char_dict

def sort_characters(char_dict):
    sorted_char = []

    for char, cnt in char_dict.items():
        sorted_char.append({"char": char, "num": cnt})
    sorted_char.sort(reverse=True, key=sort_on)
    return sorted_char

def sort_on(item):
    return item["num"]