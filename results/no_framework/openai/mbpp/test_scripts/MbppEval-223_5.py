def is_majority(arr, n, x):
    if n % 2 == 0:
        min_occurrences = n // 2 + 1
    else:
        min_occurrences = (n + 1) // 2

    count = arr.count(x)

    if count >= min_occurrences:
        return True
    else:
        return False

# Test the function




def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)