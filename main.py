def main(): 
    book_path = "books/frankenstein.txt" 
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    chars_dict = get_chars_dict(book_text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"There are {num_words} words in this book.")
    print()
    
    for item in chars_sorted_list: 
        if not item["char"].isalpha(): 
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- END REPORT ---")

### UTILITY FUNCTIONS 
    
def get_book_text(path): 
    with open(path) as f: 
        return f.read()
    
def word_count(text): 
    return len(text.split())

def get_chars_dict(text):
    char_dict = {}
    lowered = text.lower()
    for char in lowered:
        if char in char_dict: 
            char_dict[char] += 1 
        else: 
            char_dict[char] = 1
    return char_dict

def sort_on(dict): 
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict): 
    sorted_list = []
    for char in num_chars_dict: 
        sorted_list.append({"char": char, "num": num_chars_dict[char]})    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main() 