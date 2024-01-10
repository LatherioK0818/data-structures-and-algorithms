def reverseArray(arr):
    # Initialize an empty array for the reversed elements
    reversed_arr = []

    # Iterate over the original array in reverse order
    for i in range(len(arr) - 1, -1, -1):
        # Append each element to the new array
        reversed_arr.append(arr[i])

    # Return the new array
    return reversed_arr

# Example usage 
original_array = [1, 2, 3, 4, 5]
reversed_array = reverseArray(original_array)
print("Original Array:", original_array)
print("Reversed Array:", reversed_array)

