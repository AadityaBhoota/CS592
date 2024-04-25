from collections import Counter

def is_majority(arr, n, x):
    if n % 2 == 0:
        return False
    
    count_x = arr.count(x)
    if count_x > n // 2:
        return True
    return False

# Test the function


def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)