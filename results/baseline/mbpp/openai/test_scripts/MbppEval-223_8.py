def is_majority(arr, n, x):
    if arr[n//2] != x:
        return False

    first_occurrence = arr.index(x)
    last_occurrence = arr[::-1].index(x)
    
    if first_occurrence + last_occurrence >= n:
        return True
    return False

# Testing the function with the given examples




def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)