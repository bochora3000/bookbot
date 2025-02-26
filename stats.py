def count_words(book):
    list_of_words = book.split()
    return len(list_of_words)

def count_chars(book):
    character_map = {}
    
    for char in book:
        char = char.lower()
        if char not in character_map:
            character_map[char] = 1
        else:
            character_map[char] += 1
    
    return character_map

def report(character_dictionary):
    list_of_dictionaries = []
    
    for key, value in character_dictionary.items():
        if key.isalpha():
            list_of_dictionaries.append({key:value})
    
    sorted_data_desc = sorted(list_of_dictionaries, key=lambda d: list(d.values())[0], reverse=True)
    # print(sorted_data)
    
    return sorted_data_desc