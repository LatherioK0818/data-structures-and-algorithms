# test_linked_list.py

from linked_list import LinkedList

def test_linked_list():
    ll = LinkedList()
    assert ll.head is None, "Failed to instantiate an empty linked list"

    ll.insert("a")
    assert ll.head.value == "a", "Failed to properly insert into the linked list"

    ll.insert("b")
    assert ll.head.value == "b", "Head property does not point to the first node"
    assert ll.head.next.value == "a", "Failed to properly insert multiple nodes"

    assert ll.includes("a") == True, "Failed to find an existing value"
    assert ll.includes("z") == False, "Incorrectly found a non-existing value"

    assert ll.to_string() == "{ b } -> { a } -> NULL", "Failed to return proper string representation"

    print("All tests passed.")

if __name__ == "__main__":
    test_linked_list()

