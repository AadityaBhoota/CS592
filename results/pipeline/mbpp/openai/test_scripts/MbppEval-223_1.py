def is_majority(arr, n, x):
    if n <= 0:
        return False

    min_count = n // 2

    count = 0
    for num in arr:
        if num == x:
            count += 1

    if count > min_count:
        return True

    return False

def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)