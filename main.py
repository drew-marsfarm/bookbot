from stats import word_count
from stats import count_letters
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
    return book_contents 

if __name__  == "__main__":
    output = get_book_text("./books/frankenstein.txt")
    
    word_count_output = word_count(output)
    count_letters_output = count_letters(output)
    character_count_output = sort_dict(count_letters_output)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count_output} total words")
    print("--------- Character Count -------")

    for char in character_count_output:
        # each 'char' is a dictionary: {"char": "a", "num": 234}
        letter = char["char"]
        number = char["num"]
        print(f"{letter}: {number}")

    print("============= END ===============")