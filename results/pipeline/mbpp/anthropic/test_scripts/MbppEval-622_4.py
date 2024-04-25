def get_median(arr1, arr2, n):
    combined = sorted(arr1 + arr2)
    if n % 2 == 0:
        middle1 = combined[n - 1]
        middle2 = combined[n]
        median = (middle1 + middle2) / 2
    else:
        median = combined[n // 2]
    return median

def check(candidate):
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0

check(get_median)