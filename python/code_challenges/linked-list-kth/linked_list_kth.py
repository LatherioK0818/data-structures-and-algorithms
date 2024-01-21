class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def kthFromEnd(self, k):
        if k < 0:
            raise ValueError("k must be a non-negative integer")

        length = 0
        current = self.head
        while current:
            current = current.next
            length += 1

        if k >= length:
            raise ValueError("k is greater than the length of the list")

        target = length - k - 1
        current = self.head
        for i in range(target):
            current = current.next

        return current.value

# Example Usage
ll = LinkedList()
ll.append(1)
ll.append(3)
ll.append(8)
ll.append(2)

print(ll.kthFromEnd(0))  # Output: 2
print(ll.kthFromEnd(2))  # Output: 3
