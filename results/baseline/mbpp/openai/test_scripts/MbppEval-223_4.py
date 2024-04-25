def is_majority(arr, n, x):
    if n == 0:
        return False

    left = 0
    right = n - 1

    # Find the first occurrence of the element x
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid

    # Check if the element x occurs more than n/2 times
    if left + n // 2 < n and arr[left + n // 2] == x:
        return True

    return False

# Test cases




def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)