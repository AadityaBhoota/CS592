def get_median(arr1, arr2, n):
    """
    Find the median of two sorted lists of the same size.

    Args:
        arr1 (list): First sorted list.
        arr2 (list): Second sorted list.
        n (int): Size of the lists.

    Returns:
        float: Median of the two lists.
    """
    left = 0
    right = n - 1

    while True:
        if left > right:
            break

        i = (left + right) // 2
        j = n - 1 - i

        max_left_1 = arr1[i] if i >= 0 else float('-inf')
        min_right_1 = arr1[i + 1] if i + 1 < n else float('inf')

        max_left_2 = arr2[j] if j >= 0 else float('-inf')
        min_right_2 = arr2[j + 1] if j + 1 < n else float('inf')

        if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
            if (n * 2) % 2 == 0:
                return (max(max_left_1, max_left_2) + min(min_right_1, min_right_2)) / 2
            else:
                return min(min_right_1, min_right_2)
        elif max_left_1 > min_right_2:
            right = i - 1
        else:
            left = i + 1

    return 0.0

def check(candidate):
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0

check(get_median)