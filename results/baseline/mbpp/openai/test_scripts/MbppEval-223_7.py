def is_majority(arr, n, x):
    left = 0
    right = n - 1

    # Find the first occurrence of x in the array
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            break
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    if arr[mid] != x:
        return False

    # Check if x occurs more than n/2 times
    if arr[mid + n//2] == x:
        return True
    else:
        return False

# Test cases




def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)