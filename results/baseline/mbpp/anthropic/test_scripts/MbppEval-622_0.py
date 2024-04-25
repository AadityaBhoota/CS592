def get_median(arr1, arr2, n):
    if n == 0:
        return -1

    # Combine the two arrays
    merged = [0] * (2 * n)
    i, j, k = 0, 0, 0

    # Merge the two arrays
    while i < n and j < n:
        if arr1[i] < arr2[j]:
            merged[k] = arr1[i]
            i += 1
        else:
            merged[k] = arr2[j]
            j += 1
        k += 1

    # Add remaining elements from arr1 (if any)
    while i < n:
        merged[k] = arr1[i]
        i += 1
        k += 1

    # Add remaining elements from arr2 (if any)
    while j < n:
        merged[k] = arr2[j]
        j += 1
        k += 1

    # Find the median
    mid = (2 * n) // 2
    if (2 * n) % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2
    else:
        return merged[mid]

def check(candidate):
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0

check(get_median)