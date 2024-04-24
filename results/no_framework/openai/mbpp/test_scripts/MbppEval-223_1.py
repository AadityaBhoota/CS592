def is_majority(arr, n, x):
    start = 0
    end = n - 1

    # Find the first occurrence of x in the array
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == x and (mid == 0 or arr[mid-1] != x):
            first_occurrence = mid
            break
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    else:
        return False

    # Find the last occurrence of x in the array
    start = 0
    end = n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == x and (mid == n-1 or arr[mid+1] != x):
            last_occurrence = mid
            break
        elif arr[mid] <= x:
            start = mid + 1
        else:
            end = mid - 1

    if last_occurrence - first_occurrence + 1 > n // 2:
        return True
    return False

# Test cases




def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)