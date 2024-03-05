def main(): 
    book_path = "books/frankenstein.txt" 
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    num_char = char_count(book_text) 
    print(f"This text has {num_words} words.")
    print(f"And here is total count of each character: {num_char}")

### UTILITY FUNCTIONS 
    
def get_book_text(path): 
    with open(path) as f: 
        return f.read()
    
def word_count(text): 
    return len(text.split())

def char_count(text):
    char_dict = {}
    lowered = text.lower()
    for char in lowered:
        if char in char_dict: 
            char_dict[char] += 1 
        else: 
            char_dict[char] = 1
    return char_dict

main() 