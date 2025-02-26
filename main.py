from stats import count_words, count_chars, report
import sys

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_file = sys.argv[1]
    book_as_a_string = get_book_text(path_file)
    
    num_words = count_words(book_as_a_string)
    
    print(f"{num_words} words found in the document")
    
    character_dictionary = count_chars(book_as_a_string)
    
    sorted_character_count = report(character_dictionary)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character_dict in sorted_character_count:
        
        for key, value in character_dict.items():
            print(f"{key}: {value}")
    print("============= END ===============")
    
def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

main()
