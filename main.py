from stats import get_book_text, word_counter

def main():
    text = get_book_text("books/frankenstein.txt")
    num_of_words = word_counter(text)
    print(f"Found {num_of_words} total words")

main()
