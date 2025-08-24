from stats import word_count

def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
    return book_contents 

if __name__  == "__main__":
    output = get_book_text("./books/frankenstein.txt")
    
    word_count_output = word_count(output)
    
    print(f"{word_count_output} words found in the document")