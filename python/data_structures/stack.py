from data_structures.invalid_operation_error import InvalidOperationError
class Node:
    """
    Node Class:
    Represents a node in a linked list.

    Attributes:
    - value: The value stored in the node.
    - next: A pointer to the next node in the linked list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
        return self.top is None
