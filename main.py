def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
    return book_contents 

if __name__  == "__main__":
    output = get_book_text("./books/frankenstein.txt")
    print(output)