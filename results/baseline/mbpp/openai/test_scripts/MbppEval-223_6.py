def is_majority(arr, n, x):
    first_occurrence = next((i for i, val in enumerate(arr) if val == x), None)
    last_occurrence = next((i for i, val in enumerate(arr[::-1]) if val == x), None)
    
    if first_occurrence is None or last_occurrence is None:
        return False
    
    occurrences = last_occurrence - first_occurrence + 1
    return occurrences > n / 2

# Test cases




def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)