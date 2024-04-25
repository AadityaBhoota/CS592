def find_kth(arr1, arr2, k):
    """
    Find the kth element from the given two sorted arrays.

    Args:
        arr1 (List[int]): The first sorted array.
        arr2 (List[int]): The second sorted array.
        k (int): The kth element to find.

    Returns:
        int: The kth element from the two sorted arrays.
    """
    n1, n2 = len(arr1), len(arr2)
    if n1 > n2:
        arr1, arr2, n1, n2 = arr2, arr1, n2, n1

    left, right = 0, n1

    while left <= right:
        partition1 = (left + right) // 2
        partition2 = k - partition1

        max_left1 = arr1[partition1 - 1] if partition1 != 0 else float('-inf')
        min_right1 = arr1[partition1] if partition1 != n1 else float('inf')

        max_left2 = arr2[partition2 - 1] if partition2 != 0 else float('-inf')
        min_right2 = arr2[partition2] if partition2 != n2 else float('inf')

        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if (k == 1):
                return min(arr1[0], arr2[0])
            return max(max_left1, max_left2)
        elif max_left1 > min_right2:
            right = partition1 - 1
        else:
            left = partition1 + 1

    return -1  # k is out of range

def check(candidate):
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8

check(find_kth)