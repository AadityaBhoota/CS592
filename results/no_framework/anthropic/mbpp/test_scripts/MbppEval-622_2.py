def get_median(arr1, arr2, n):
    """
    Write a function to find the median of two sorted lists of same size.

    Examples:
    get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0
    """
    # Combine the two arrays into one
    merged = []
    i, j = 0, 0
    while i < n and j < n:
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Add remaining elements from the first array, if any
    while i < n:
        merged.append(arr1[i])
        i += 1
    
    # Add remaining elements from the second array, if any
    while j < n:
        merged.append(arr2[j])
        j += 1
    
    # Find the median
    middle = len(merged) // 2
    if len(merged) % 2 == 0:
        return (merged[middle - 1] + merged[middle]) / 2
    else:
        return merged[middle]

def check(candidate):
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0

check(get_median)