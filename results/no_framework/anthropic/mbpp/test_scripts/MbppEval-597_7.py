def find_kth(arr1, arr2, k):
    """
    Write a function to find the kth element from the given two sorted arrays.

    Args:
        arr1 (list): The first sorted array.
        arr2 (list): The second sorted array.
        k (int): The kth element to find.

    Returns:
        int: The kth element from the two sorted arrays.
    """
    m, n = len(arr1), len(arr2)
    if m > n:
        arr1, arr2, m, n = arr2, arr1, n, m

    left, right = 0, m

    while left <= right:
        partition_x = (left + right) // 2
        partition_y = k - partition_x

        max_left_x = arr1[partition_x - 1] if partition_x != 0 else float('-inf')
        min_right_x = arr1[partition_x] if partition_x != m else float('inf')

        max_left_y = arr2[partition_y - 1] if partition_y != 0 else float('-inf')
        min_right_y = arr2[partition_y] if partition_y != n else float('inf')

        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            return max(max_left_x, max_left_y)
        elif max_left_x > min_right_y:
            right = partition_x - 1
        else:
            left = partition_x + 1

    return -1

def check(candidate):
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8

check(find_kth)