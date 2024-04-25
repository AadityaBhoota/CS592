def get_median(arr1, arr2, n):
    i, j = 0, 0
    count = 0
    median = 0

    while i < n and j < n:
        if arr1[i] < arr2[j]:
            count += 1
            if count == (n - 1) // 2:
                median = arr1[i]
            i += 1
        else:
            count += 1
            if count == (n - 1) // 2:
                median = arr2[j]
            j += 1

    if n % 2 == 0:
        if i < n:
            median = (median + arr1[i]) / 2
        else:
            median = (median + arr2[j]) / 2

    return median

def check(candidate):
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0

check(get_median)