def reverseArray(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

import unittest

class TestReverseArray(unittest.TestCase):

    def test_standard_case(self):
        self.assertEqual(reverseArray([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_empty_array(self):
        self.assertEqual(reverseArray([]), [])

    def test_single_element(self):
        self.assertEqual(reverseArray([42]), [42])

    def test_two_elements(self):
        self.assertEqual(reverseArray([1, 2]), [2, 1])

    def test_reversed_input(self):
        self.assertEqual(reverseArray([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()

