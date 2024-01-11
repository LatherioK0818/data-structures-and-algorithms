import pytest

def insertShiftArray(arr, value):
    middle_index = (len(arr) + 1) // 2
    new_array = [0] * (len(arr) + 1)
    for i in range(middle_index):
        new_array[i] = arr[i]
    new_array[middle_index] = value
    for i in range(middle_index, len(arr)):
        new_array[i + 1] = arr[i]
    return new_array

# Happy path tests
def test_insert_middle_even():
    arr = [2, 4, 6, 8]
    value = 5
    expected = [2, 4, 5, 6, 8]
    actual = insertShiftArray(arr, value)
    assert actual == expected

def test_insert_middle_odd():
    arr = [1, 3, 5, 7]
    value = 4
    expected = [1, 3, 4, 5, 7]
    actual = insertShiftArray(arr, value)
    assert actual == expected

def test_insert_beginning():
    arr = [4, 6, 8]
    value = 2
    expected = [2, 4, 6, 8]
    actual = insertShiftArray(arr, value)
    assert actual == expected

def test_insert_end():
    arr = [2, 4, 6]
    value = 8
    expected = [2, 4, 6, 8]
    actual = insertShiftArray(arr, value)
    assert actual == expected

# Expected failure tests
def test_invalid_array_type():
    arr = "hello"
    value = 5
    with pytest.raises(TypeError):
        insertShiftArray(arr, value)

def test_invalid_value_type():
    arr = [1, 3, 5]
    value = "apple"
    with pytest.raises(TypeError):
        insertShiftArray(arr, value)

# Edge case tests
def test_insert_empty_array():
    arr = []
    value = 10
    expected = [10]
    actual = insertShiftArray(arr, value)
    assert actual == expected

def test_insert_duplicate_value():
    arr = [2, 4, 6, 6]
    value = 6
    expected = [2, 4, 6, 6, 6]
    actual = insertShiftArray(arr, value)
    assert actual == expected
