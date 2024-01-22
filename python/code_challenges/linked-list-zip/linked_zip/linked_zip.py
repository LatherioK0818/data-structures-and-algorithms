class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, values=None):  # Accept an optional `values` list
        self.head = None
        if values:
            self.add_multiple(values)

    def zip_lists(list1, list2):
        if list1 is None or list1.head is None:
            return list2
        if list2 is None or list2.head is None:
            return list1

        zipped_list = LinkedList()
        zipped_list.head = list1.head

        current1 = list1.head
        current2 = list2.head
        while current1 is not None and current2 is not None:
            next1 = current1.next
            next2 = current2.next

            current1.next = current2
            if next1 is not None:
                current2.next = next1

            current1 = next1
            current2 = next2

        # Append remaining nodes from the longer list
        if current1 is None and current2 is not None:
            # Find the last node in the zipped list
            last_node = zipped_list.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = current2

        return zipped_list
