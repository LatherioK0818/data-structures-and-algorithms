import unittest
from linked_list_module import LinkedList, TargetError  # Replace with your actual file and class names

class TestLinkedList(unittest.TestCase):

    def test_insert_at_beginning(self):
        ll = LinkedList()
        ll.insert(1)
        self.assertEqual(str(ll), "{ 1 } -> NULL", "Should insert 1 at the beginning of the list")

    def test_append_to_end(self):
        ll = LinkedList()
        ll.append(1)
        self.assertEqual(str(ll), "{ 1 } -> NULL", "Should append 1 at the end of the list")

    def test_append_multiple_nodes(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        self.assertEqual(str(ll), "{ 1 } -> { 2 } -> NULL", "Should append 1 and 2 at the end of the list")

    def test_insert_before_middle(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(3)
        ll.insert_before(3, 2)
        self.assertEqual(str(ll), "{ 1 } -> { 2 } -> { 3 } -> NULL", "Should insert 2 before 3")

    def test_insert_before_first(self):
        ll = LinkedList()
        ll.append(2)
        ll.insert_before(2, 1)
        self.assertEqual(str(ll), "{ 1 } -> { 2 } -> NULL", "Should insert 1 before 2")

    def test_insert_after_middle(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(4)
        ll.insert_after(2, 3)
        self.assertEqual(str(ll), "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> NULL", "Should insert 3 after 2")

    def test_insert_after_last(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.insert_after(2, 3)
        self.assertEqual(str(ll), "{ 1 } -> { 2 } -> { 3 } -> NULL", "Should insert 3 after 2")

    def test_insert_before_in_empty_list(self):
        ll = LinkedList()
        with self.assertRaises(TargetError):
            ll.insert_before(1, 0)

    def test_insert_after_in_empty_list(self):
        ll = LinkedList()
        with self.assertRaises(TargetError):
            ll.insert_after(1, 2)

    def test_insert_before_nonexistent_value(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        with self.assertRaises(TargetError):
            ll.insert_before(3, 0)

    def test_insert_after_nonexistent_value(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        with self.assertRaises(TargetError):
            ll.insert_after(3, 0)

if __name__ == '__main__':
    unittest.main()
