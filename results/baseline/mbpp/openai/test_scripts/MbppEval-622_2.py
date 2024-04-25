def get_median(arr1, arr2, n):
    merged_arr = arr1 + arr2
    merged_arr.sort()

    if n % 2 != 0:
        return float(merged_arr[n // 2])
    else:
        mid = n // 2
        return (merged_arr[mid - 1] + merged_arr[mid]) / 2.0

# Examples




def check(candidate):
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0

check(get_median)