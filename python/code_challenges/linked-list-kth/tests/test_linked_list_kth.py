import unittest
from linked_list_kth import LinkedList  # Replace with your actual file and class names

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_add_node_to_end(self):
        self.ll.append(1)
        self.assertEqual(self.ll.tail.value, 1)  # Assuming your LinkedList has a tail property

    def test_add_multiple_nodes_to_end(self):
        self.ll.append(1)
        self.ll.append(2)
        self.assertEqual(self.ll.tail.value, 2)
        self.assertEqual(self.ll.head.next.value, 2)  # Assuming your LinkedList has a head property

    def test_insert_node_in_middle(self):
        self.ll.append(1)
        self.ll.append(3)
        self.ll.insert_before(3, 2)  # Assuming you have an insert_before method
        self.assertEqual(self.ll.head.next.value, 2)

    def test_insert_node_before_first(self):
        self.ll.append(1)
        self.ll.insert_before(1, 0)
        self.assertEqual(self.ll.head.value, 0)

    def test_insert_after_middle_node(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(4)
        self.ll.insert_after(2, 3)  # Assuming you have an insert_after method
        self.assertEqual(self.ll.head.next.next.value, 3)

    def test_insert_after_last_node(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.insert_after(2, 3)
        self.assertEqual(self.ll.tail.value, 3)

    # ... any additional tests ...

if __name__ == '__main__':
    unittest.main()
