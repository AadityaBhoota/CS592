def is_majority(arr, n, x):
    """
    Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)

    Examples:
    is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    is_majority([1, 1, 1, 2, 2], 5, 1) == True
    """
    # Find the first and last index of the element x in the sorted array
    first_idx = _find_first_idx(arr, 0, n - 1, x)
    last_idx = _find_last_idx(arr, 0, n - 1, x)

    # Check if the element occurs more than n/2 times
    return (last_idx - first_idx + 1) > (n // 2)


def _find_first_idx(arr, low, high, x):
    """
    Helper function to find the first index of the element x in the sorted array
    """
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            if mid == 0 or arr[mid - 1] != x:
                return mid
            else:
                high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def _find_last_idx(arr, low, high, x):
    """
    Helper function to find the last index of the element x in the sorted array
    """
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            if mid == len(arr) - 1 or arr[mid + 1] != x:
                return mid
            else:
                low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)