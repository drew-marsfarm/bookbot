def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
    return book_contents 

def word_count(string):
    process1 = string.split()
    length = len(process1)
    return length

if __name__  == "__main__":
    #output = get_book_text("./books/frankenstein.txt")
    with open("./books/frankenstein.txt") as book:
        output = word_count(book)
    print(f"{output} words found in the document")