# Zip Two Linked Lists
This challenge involves writing a function that takes two linked lists and zips them into a single linked list, alternating between nodes from each list.

## Whiteboard Process
![Whiteboard Solution](path/to/your/whiteboard/image)

## Approach & Efficiency
The approach taken for this challenge is to traverse both linked lists simultaneously, connecting nodes from each list alternatively to form a new linked list. This approach ensures that the space complexity remains O(1), as it only creates a few pointers without allocating any additional nodes. The time complexity of this approach is O(n), where n is the length of the longer linked list, since we have to traverse each list only once.

## Solution

```python
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:

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
```

Example Usage:
```python
# Assuming list1 and list2 are LinkedList instances
zipped_list = zipLists(list1, list2)
print(zipped_list)
```
