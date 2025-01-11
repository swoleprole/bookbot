def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    sorted_chars = sorted(chars_dict.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars: 
        char_display = char
        print(f"The '{char_display}' character was found {count} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():  # Only process the character if it's a letter
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()