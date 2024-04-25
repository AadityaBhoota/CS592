def is_majority(arr, n, x):
    # Find the first and last index of x in the sorted array
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == x:
            break
        elif arr[mid] < x:
            first = mid + 1
        else:
            last = mid - 1

    # If x is not found in the array, return False
    if arr[mid] != x:
        return False

    # Find the first index of x
    start = mid
    while start > 0 and arr[start - 1] == x:
        start -= 1

    # Find the last index of x
    end = mid
    while end < n - 1 and arr[end + 1] == x:
        end += 1

    # Check if the count of x is greater than n/2
    if end - start + 1 > n // 2:
        return True
    else:
        return False

def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)