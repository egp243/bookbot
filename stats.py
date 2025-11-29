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