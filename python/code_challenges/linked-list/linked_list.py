class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        values = []
        current = self.head
        while current:
            values.append(f"{{ {current.value} }}")
            current = current.next
        values.append("NULL")
        return " -> ".join(values)

# Example Usage
linked_list = LinkedList()
linked_list.insert("a")
linked_list.insert("b")
linked_list.insert("c")

print(linked_list.to_string())  # { c } -> { b } -> { a } -> NULL
print(linked_list.includes("a"))  # True
print(linked_list.includes("z"))  # False
