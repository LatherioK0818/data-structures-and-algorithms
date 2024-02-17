class Hashtable:
    """
    A simple implementation of a Hashtable that supports basic operations such as:
    - Setting a key/value pair
    - Getting the value by key
    - Checking if a key exists
    - Listing all keys
    - Hashing a key to an index
    This implementation handles collisions using chaining.
    """

    def __init__(self, size=100):
        """
        Initializes the hashtable with a specified size and sets up the storage for the key/value pairs.
        """
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        """
        Generates a hash for a given key and maps it to an index within the table's size.
        """
        return sum(ord(char) for char in key) % self.size

    def set(self, key, value):
        """
        Sets a key/value pair in the hashtable. If the key already exists, its value is updated.
        Handles collisions through chaining.
        """
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = []

        # Check for an existing key and update the value
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        """
        Retrieves the value associated with a given key from the hashtable.
        Returns None if the key does not exist.
        """
        index = self.hash(key)
        if self.table[index] is None:
            return None

        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def has(self, key):
        """
        Checks if the given key exists in the hashtable.
        Returns a boolean value.
        """
        index = self.hash(key)
        if self.table[index] is None:
            return False

        for k, _ in self.table[index]:
            if k == key:
                return True
        return False

    def keys(self):
        """
        Returns a collection of all the keys present in the hashtable.
        """
        keys_list = []
        for item in self.table:
            if item:
                keys_list.extend(k for k, _ in item)
        return keys_list
