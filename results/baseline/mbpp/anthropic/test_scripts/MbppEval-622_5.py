def get_median(arr1, arr2, n):
    """
    Find the median of two sorted lists of the same size.

    Args:
        arr1 (list): The first sorted list.
        arr2 (list): The second sorted list.
        n (int): The size of the lists.

    Returns:
        float: The median of the two lists.
    """
    # Initialize pointers for both lists
    i, j = 0, 0
    merged = []

    # Merge the two lists into a single sorted list
    while i < n and j < n:
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Append the remaining elements from either list
    while i < n:
        merged.append(arr1[i])
        i += 1

    while j < n:
        merged.append(arr2[j])
        j += 1

    # Calculate the median of the merged list
    mid = len(merged) // 2
    if len(merged) % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2
    else:
        return merged[mid]

def check(candidate):
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0

check(get_median)