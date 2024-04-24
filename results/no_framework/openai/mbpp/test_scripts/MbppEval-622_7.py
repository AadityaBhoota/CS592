def get_median(arr1, arr2, n):
    merged = sorted(arr1 + arr2)
    middle = n
    if middle % 2 == 0:
        return (merged[middle // 2 - 1] + merged[middle // 2]) / 2
    else:
        return float(merged[middle // 2])

def check(candidate):
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0

check(get_median)