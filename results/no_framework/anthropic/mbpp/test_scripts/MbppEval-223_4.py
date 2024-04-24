def is_majority(arr, n, x):
    """
    Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)

    Examples:
    is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    is_majority([1, 1, 1, 2, 2], 5, 1) == True
    """
    # Find the first and last occurrence of the element
    first = _find_first_occurrence(arr, n, x)
    last = _find_last_occurrence(arr, n, x)

    # Check if the element is the majority element
    if last - first + 1 > n // 2:
        return True
    else:
        return False

def _find_first_occurrence(arr, n, x):
    """
    Helper function to find the first occurrence of the element x in the sorted array arr.
    """
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            if mid == 0 or arr[mid - 1] != x:
                return mid
            else:
                right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def _find_last_occurrence(arr, n, x):
    """
    Helper function to find the last occurrence of the element x in the sorted array arr.
    """
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            if mid == n - 1 or arr[mid + 1] != x:
                return mid
            else:
                left = mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)