def main():
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()
    
    print("--- Begin report of books/frankenstein.txt ---")
    
    print(f"{word_counter(book_contents)} words found in the document")
    
    print("")
    
    book_characters = character_counter(book_contents)
    
    for key, value in book_characters.items():
        print(f"The '{key}' character was found {value} times")
    
    print("--- End report ---")


def word_counter(book_as_a_string):
    
    list_of_words = book_as_a_string.split()
    
    return len(list_of_words)

def character_counter(book_as_a_string):
    
    character_map = {}
    
    for char in book_as_a_string.lower():
        if char not in character_map:
            character_map[char] = 1
        else:
            character_map[char] +=1
    
    return character_map




main()