def word_count(string):
    separate_words_to_list = string.split()
    count = len(separate_words_to_list)
    return count

def count_letters(string):
    lowercase = string.lower()
    letters = ["a", "b", "C", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for letter in letters:
        instance = lowercase.count(letter)
        print(f"{letter}: {instance}")