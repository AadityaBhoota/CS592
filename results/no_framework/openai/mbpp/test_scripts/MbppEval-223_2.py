def is_majority(arr, n, x):
    mid = n // 2
    left = 0
    right = n - 1

    # Find the first occurrence of x in the sorted array
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            break
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    # Check if x is the majority element
    if mid + n // 2 < n and arr[mid] == arr[mid + n // 2]:
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