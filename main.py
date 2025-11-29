from stats import get_book_text, word_counter, char_counter, sort_characters

def main():
    text = get_book_text("books/frankenstein.txt")
    num_of_words = word_counter(text)
    print(f"Found {num_of_words} total words")
    char_dict = char_counter(text)
    print(char_dict)
    sorted_chars = sort_characters(char_dict)

    for i in sorted_chars:
        char = i["char"]
        count = i["num"]
        if char.isalpha():
            print(f"{char}: {count}")

main()
