def get_book_text(path):
    with open(path) as book:
        book_contents = book.read()
        return book_contents

def word_counter(text):
    count_words = text.split()
    return len(count_words)