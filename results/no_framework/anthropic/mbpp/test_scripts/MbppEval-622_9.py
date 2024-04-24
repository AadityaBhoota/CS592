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
    # Combine the two lists into a single sorted list
    combined_list = sorted(arr1 + arr2)

    # Find the middle index of the combined list
    middle_index = n

    # Calculate the median
    if n % 2 == 0:
        # If the size is even, the median is the average of the two middle elements
        return (combined_list[middle_index - 1] + combined_list[middle_index]) / 2
    else:
        # If the size is odd, the median is the middle element
        return combined_list[middle_index - 1]

def check(candidate):
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0

check(get_median)