from stats import get_book_text, word_counter, char_counter, sort_characters

def main():
    # 1. Get the text from the file
    text = get_book_text("books/frankenstein.txt")

    # 2. Calculate and print the total word count
    num_of_words = word_counter(text)
    print(f"Found {num_of_words} total words")

    # 3. Count character usage
    char_dict = char_counter(text)
    # (Optional: You can print the raw dictionary if you want to debug)
    # print(char_dict) 

    # 4. Convert the dictionary to a sorted list
    sorted_chars = sort_characters(char_dict)

    # 5. Loop through the sorted list and print only the alphabet characters
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words} words found in the document")
    print() # Prints a blank line
    
    for i in sorted_chars:
        char = i["char"]
        count = i["num"]
        
        # We only want to print letters, not symbols or spaces
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
            
    print("--- End report ---")

main()