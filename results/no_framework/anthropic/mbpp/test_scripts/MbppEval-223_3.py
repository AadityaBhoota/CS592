def is_majority(arr, n, x):
    """
    Determine whether the given element 'x' is the majority element in the sorted array 'arr' of length 'n'.

    Args:
        arr (list): The sorted array.
        n (int): The length of the array.
        x (int): The element to check for majority.

    Returns:
        bool: True if 'x' is the majority element, False otherwise.
    """
    # Find the first occurrence of 'x' in the array
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            break
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    # If 'x' is not present in the array, return False
    if left > right:
        return False

    # Count the number of occurrences of 'x' in the array
    count = 1
    i = mid - 1
    while i >= 0 and arr[i] == x:
        count += 1
        i -= 1
    i = mid + 1
    while i < n and arr[i] == x:
        count += 1
        i += 1

    # Check if 'x' is the majority element
    return count > n // 2

def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)