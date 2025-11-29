def get_book_text(path):
    with open(path) as book:
        book_contents = book.read()
        return book_contents

def word_counter(text):
    count_words = text.split()
    return len(count_words)

def main():
    text = get_book_text("books/frankenstein.txt")
    num_of_words = word_counter(text)
    print(f"Found {num_of_words} total words")

main()
