def is_majority(arr, n, x):
    # Find the first occurrence of x
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            if mid == 0 or arr[mid-1] != x:
                break
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    # If x is not present in the array, return False
    if left > right:
        return False
    
    # Find the last occurrence of x
    start = mid
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            if mid == n-1 or arr[mid+1] != x:
                break
            left = mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    # Calculate the number of occurrences of x
    count = mid - start + 1
    
    # Check if count is greater than n//2
    return count > n // 2

def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)