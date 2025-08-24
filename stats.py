def word_count(string):
    separate_words_to_list = string.split()
    count = len(separate_words_to_list)
    return count

def count_letters(string):
    lowercase = string.lower()
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "æ", "â", "ê", "ë", "ô"]
    letter_dict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0, "æ": 0, "â": 0, "ê": 0, "ë": 0, "ô": 0}
    for letter in letters:
        instance = lowercase.count(letter)
        letter_dict[letter] = instance
    return letter_dict

def sort_dict(dictionary):
    def sort_on(items):
        return items["num"]
    
    unsorted_dict = []

    for char in dictionary:
        number = dictionary[char]
        unsorted_dict.append(
            {"char": char, "num": number}
        )

    #sorted_dict = unsorted_dict.sort(reverse=True, key=sort_on)
    unsorted_dict.sort(reverse=True, key=sort_on)
    return unsorted_dict
