import pytest
from data_structures.hashtable import Hashtable

def test_exists():
    assert Hashtable

def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    for item in hashtable.table:
        if item:
            actual.append([(k, v) for k, v in item])
