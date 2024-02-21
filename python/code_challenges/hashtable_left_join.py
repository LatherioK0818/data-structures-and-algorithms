from data_structures.hashtable import Hashtable

def left_join(synonyms, antonyms):
    """
    Joins two hash tables (dictionaries in Python) on their keys, combining synonyms and antonyms.
    """
    results = []

    for key in synonyms.keys():
        synonym = synonyms[key]
        antonym = antonyms.get(key, None)  # Use None to represent missing antonyms, as per requirement
        results.append([key, synonym, antonym])

    # Assuming no specific order is required beyond what is given by the synonyms table
    return results
