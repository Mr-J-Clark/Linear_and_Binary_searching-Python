def linear_search(arr, target):
    """
    Perform a linear search on the array to find the target, South Park style!

    Parameters:
    arr (list): The list of elements to search, like all the craziness in South Park.
    target (any): The element to search for, just like searching for Cartman's missing snack.

    Returns:
    int: The index of the target in the array, or -1 if not found (like when Kyle can't find his hat).
    """
    for index in range(len(arr)):  # Loop through each element in the array
        if arr[index] == target:   # If we found what we're looking for, sweet!
            return index            # Return the index, kind of like giving Stan a high five
    return -1  # Return -1 if we can't find our target, just like when Cartman loses a bet.

def binary_search(arr, target):
    """
    Perform a binary search on the sorted array to find the target, South Park style!

    Parameters:
    arr (list): The sorted list of elements to search, like the chaos of the boys' adventures.
    target (any): The element to search for, as important as finding Chef's advice.

    Returns:
    int: The index of the target in the array, or -1 if not found (just like when Butters is trying to be brave).
    """
    left, right = 0, len(arr) - 1  # Initialize the left and right pointers

    while left <= right:  # Keep searching while we're still in the zone
        mid = left + (right - left) // 2  # Calculate the middle index, it’s like deciding which side to take in a fight

        if arr[mid] == target:  # If the middle element is the target, awesome!
            return mid          # Return the middle index, just like giving Kenny a thumbs up
        elif arr[mid] < target:  # If the target is greater than the middle element
            left = mid + 1      # Move the left pointer, just like moving on from Mr. Garrison’s craziness
        else:                   # If the target is less than the middle element
            right = mid - 1     # Move the right pointer, like running away from a Mr. Mackey lecture

    return -1  # Return -1 if we can't find our target, like when the boys can't find a ride home.


# Example array for linear search on numbers
arr_linear = [5, 3, 2, 8, 6]
target_linear = 8
result_linear = linear_search(arr_linear, target_linear)
print(f"Linear Search: Target {target_linear} found at index {result_linear}.")

# Example array for binary search (must be sorted)
arr_binary = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_binary = 5
result_binary = binary_search(arr_binary, target_binary)
print(f"Binary Search: Target {target_binary} found at index {result_binary}.")


# Example array for linear search
arr_linear = ['Cartman', 'Stan', 'Kyle', 'Kenny']
target_linear = 'Kenny'
result_linear = linear_search(arr_linear, target_linear)
print(f"Linear Search: Target '{target_linear}' found at index {result_linear}. You go, Kenny!")

# Example array for binary search (must be sorted)
arr_binary = ['Butters', 'Cartman', 'Kenny', 'Stan']
arr_binary.sort()  # Sort the array, like making peace in South Park
target_binary = 'Stan'
result_binary = binary_search(arr_binary, target_binary)
print(f"Binary Search: Target '{target_binary}' found at index {result_binary}. Hooray for Stan!")