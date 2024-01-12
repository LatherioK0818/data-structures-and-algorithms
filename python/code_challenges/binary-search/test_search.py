import unittest
from binary_search import BinarySearch

class TestBinarySearch(unittest.TestCase):

    def test_find_key_in_middle(self):
        arr = [2, 3, 4, 10, 40]
        key = 10
        self.assertEqual(BinarySearch(arr, key), 3)

    def test_find_first_key(self):
        arr = [2, 3, 4, 4, 40]
        key = 2
        self.assertEqual(BinarySearch(arr, key), 0)

    def test_find_last_key(self):
        arr = [2, 3, 4, 4, 40]
        key = 40
        self.assertEqual(BinarySearch(arr, key), 4)

    def test_key_not_found(self):
        arr = [2, 3, 4, 10, 40]
        key = 5
        self.assertEqual(BinarySearch(arr, key), -1)

    def test_empty_array(self):
        arr = []
        key = 10
        self.assertEqual(BinarySearch(arr, key), -1)

    def test_single_element_array(self):
        arr = [10]
        key = 10
        self.assertEqual(BinarySearch(arr, key), 0)
        key = 5
        self.assertEqual(BinarySearch(arr, key), -1)

    def test_unsorted_array(self):
        arr = [40, 2, 4, 10, 3]
        key = 4
        self.assertEqual(BinarySearch(arr, key), -1)  # Binary search only works on sorted arrays

    def test_large_array(self):
        import random
        arr = list(range(10000))  # Generate a large array
        key = random.randint(0, 9999)  # Choose a random key within the array
        self.assertEqual(BinarySearch(arr, key), key)  # Assert that the key is found at its correct index

if __name__ == '__main__':
    unittest.main()
