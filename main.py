def get_book_text(path):
    with open(path) as book:
        book_contents = book.read()
        return book_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)

main()
