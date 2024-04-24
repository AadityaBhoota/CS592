def is_majority(arr, n, x):
    """
    Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)

    Examples:
    is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    is_majority([1, 1, 1, 2, 2], 5, 1) == True
    """
    # Find the first and last occurrence of the element in the sorted array
    first = _find_first_occurrence(arr, n, x)
    last = _find_last_occurrence(arr, n, x)

    # Check if the count of the element is greater than n/2
    return (last - first + 1) > (n // 2)

def _find_first_occurrence(arr, n, x):
    """
    Helper function to find the first occurrence of the element in the sorted array.
    """
    left, right = 0, n - 1
    first_occurrence = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            first_occurrence = mid
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return first_occurrence

def _find_last_occurrence(arr, n, x):
    """
    Helper function to find the last occurrence of the element in the sorted array.
    """
    left, right = 0, n - 1
    last_occurrence = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            last_occurrence = mid
            left = mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return last_occurrence

def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)