def is_majority(arr, n, x):
    # Find the first and last index of x in the sorted array
    first_index = 0
    last_index = n - 1
    while first_index <= last_index:
        mid = (first_index + last_index) // 2
        if arr[mid] == x:
            break
        elif arr[mid] < x:
            first_index = mid + 1
        else:
            last_index = mid - 1
    
    # If x is not present in the array, return False
    if arr[first_index] != x:
        return False
    
    # Calculate the count of x
    count = last_index - first_index + 1
    
    # Check if x is the majority element
    return count > n // 2

def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)