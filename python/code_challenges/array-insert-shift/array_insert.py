def insertShiftArray(arr, value):
    middle_index = (len(arr) + 1) // 2
    new_array = [0] * (len(arr) + 1)

    for i in range(middle_index):
        new_array[i] = arr[i]

    new_array[middle_index] = value

    for i in range(middle_index, len(arr)):
        new_array[i + 1] = arr[i]

    return new_array
