def is_majority(arr, n, x):
    """
    Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)

    Examples:
    is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    is_majority([1, 1, 1, 2, 2], 5, 1) == True
    """
    first_occurrence = find_first_occurrence(arr, x)
    if first_occurrence == -1:
        return False
    last_occurrence = find_last_occurrence(arr, x)
    return (last_occurrence - first_occurrence + 1) > n // 2

def find_first_occurrence(arr, x):
    """
    Helper function to find the first occurrence of an element in a sorted array.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            if mid == 0 or arr[mid-1] != x:
                return mid
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_last_occurrence(arr, x):
    """
    Helper function to find the last occurrence of an element in a sorted array.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            if mid == len(arr) - 1 or arr[mid+1] != x:
                return mid
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