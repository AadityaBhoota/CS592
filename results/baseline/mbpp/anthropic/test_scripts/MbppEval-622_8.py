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

    # Add remaining elements from arr1, if any
    while i < n:
        merged_list.append(arr1[i])
        i += 1

    # Add remaining elements from arr2, if any
    while j < n:
        merged_list.append(arr2[j])
        j += 1

    length = len(merged_list)
    if length % 2 == 0:
        middle1 = length // 2 - 1
        middle2 = length // 2
        median = (merged_list[middle1] + merged_list[middle2]) / 2
    else:
        middle = length // 2
        median = merged_list[middle]

    return median

def check(candidate):
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0

check(get_median)