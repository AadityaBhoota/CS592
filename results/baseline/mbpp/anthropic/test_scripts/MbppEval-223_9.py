def is_majority(arr, n, x):
    """
    Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)

    Examples:
    is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    is_majority([1, 1, 1, 2, 2], 5, 1) == True
    """
    # Find the first and last occurrence of the element in the sorted array
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == x:
            # Check if the element is the majority element
            if (mid == 0 or arr[mid - 1] != x) and (mid == n - 1 or arr[mid + 1] != x):
                return mid * 2 > n
            elif arr[mid] > x:
                last = mid - 1
            else:
                first = mid + 1
        elif arr[mid] > x:
            last = mid - 1
        else:
            first = mid + 1
    return False

def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)