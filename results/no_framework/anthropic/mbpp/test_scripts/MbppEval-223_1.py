def is_majority(arr, n, x):
    """
    Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)

    Examples:
    is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    is_majority([1, 1, 1, 2, 2], 5, 1) == True
    """
    # Find the first and last occurrence of the element
    first = _find_first_occurrence(arr, 0, n-1, x)
    if first == -1:
        return False
    last = _find_last_occurrence(arr, first, n-1, x)

    # Check if the element occurs more than n/2 times
    return (last - first + 1) > n // 2

def _find_first_occurrence(arr, low, high, x):
    """
    Helper function to find the first occurrence of the element in the sorted array.
    """
    if high >= low:
        mid = low + (high - low) // 2
        if (mid == 0 or x > arr[mid-1]) and arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return _find_first_occurrence(arr, mid+1, high, x)
        else:
            return _find_first_occurrence(arr, low, mid-1, x)
    return -1

def _find_last_occurrence(arr, low, high, x):
    """
    Helper function to find the last occurrence of the element in the sorted array.
    """
    if high >= low:
        mid = low + (high - low) // 2
        if (mid == len(arr)-1 or x < arr[mid+1]) and arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return _find_last_occurrence(arr, low, mid-1, x)
        else:
            return _find_last_occurrence(arr, mid+1, high, x)
    return -1

def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)