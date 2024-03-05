def main(): 
    book_path = "books/frankenstein.txt" 
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    print(num_words)
    
def get_book_text(path): 
    with open(path) as f: 
        return f.read()
    
def word_count(text): 
    return len(text.split())


main()