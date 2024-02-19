from data_structures.hashtable import Hashtable


def first_repeated_word(input_string):
    hashtable = Hashtable(size=100) 
    words = input_string.lower().split()
    for word in words:

        word = ''.join(char for char in word if char.isalnum())

        if hashtable.has(word):
            return word
        hashtable.set(word, True)

    return None
