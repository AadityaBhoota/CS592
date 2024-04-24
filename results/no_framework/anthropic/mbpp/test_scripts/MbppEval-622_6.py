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
    i = 0
    j = 0

    # Create a merged list to store the combined elements
    merged = []

    # Merge the two lists until the size of the merged list is equal to 2 * n
    while len(merged) < 2 * n:
        # If the current element in arr1 is smaller, add it to the merged list
        if i < n and (j >= n or arr1[i] < arr2[j]):
            merged.append(arr1[i])
            i += 1
        # Otherwise, add the current element in arr2 to the merged list
        else:
            merged.append(arr2[j])
            j += 1

    # Calculate the median based on the size of the merged list
    if len(merged) % 2 == 0:
        return (merged[n - 1] + merged[n]) / 2
    else:
        return merged[n]

def check(candidate):
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0

check(get_median)