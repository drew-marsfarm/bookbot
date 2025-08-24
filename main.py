from stats import word_count

def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
    return book_contents 

if __name__  == "__main__":
    #output = get_book_text("./books/frankenstein.txt")
    with open("./books/frankenstein.txt") as book:
        book_contents = book.read()
        output = word_count(book_contents)
    print(f"{output} words found in the document")