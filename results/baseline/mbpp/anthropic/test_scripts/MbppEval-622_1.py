def get_median(arr1, arr2, n):
    """
    Write a function to find the median of two sorted lists of same size.

    Examples:
    get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0
    """
    i = 0
    j = 0
    merged_list = []

    while i < n and j < n:
        if arr1[i] < arr2[j]:
            merged_list.append(arr1[i])
            i += 1
        else:
            merged_list.append(arr2[j])
            j += 1

    while i < n:
        merged_list.append(arr1[i])
        i += 1

    while j < n:
        merged_list.append(arr2[j])
        j += 1

    median_index = n * 2 // 2
    if n * 2 % 2 == 0:
        return (merged_list[median_index - 1] + merged_list[median_index]) / 2
    else:
        return merged_list[median_index]

def check(candidate):
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0

check(get_median)