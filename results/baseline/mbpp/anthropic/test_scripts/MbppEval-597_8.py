def find_kth(arr1, arr2, k):
    """
    Write a function to find the kth element from the given two sorted arrays.

    Args:
        arr1 (list): The first sorted array.
        arr2 (list): The second sorted array.
        k (int): The index of the element to find (1-indexed).

    Returns:
        int: The kth element from the two sorted arrays.
    """
    m, n = len(arr1), len(arr2)
    if m > n:
        arr1, arr2, m, n = arr2, arr1, n, m

    left, right = 0, m

    while left <= right:
        partition1 = (left + right) // 2
        partition2 = k - partition1

        # Handle edge cases
        max_of_left1 = arr1[partition1 - 1] if partition1 != 0 else float('-inf')
        min_of_right1 = arr1[partition1] if partition1 != m else float('inf')
        max_of_left2 = arr2[partition2 - 1] if partition2 != 0 else float('-inf')
        min_of_right2 = arr2[partition2] if partition2 != n else float('inf')

        if max_of_left1 <= min_of_right2 and max_of_left2 <= min_of_right1:
            if (m + n + 1) // 2 == k:
                return max(max_of_left1, max_of_left2)
            elif (m + n + 1) // 2 < k:
                left = partition1 + 1
            else:
                right = partition1 - 1
        elif max_of_left1 > min_of_right2:
            right = partition1 - 1
        else:
            left = partition1 + 1

    raise ValueError("Invalid input: k is out of range")

def check(candidate):
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8

check(find_kth)