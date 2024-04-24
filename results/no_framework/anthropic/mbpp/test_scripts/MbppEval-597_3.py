def find_kth(arr1, arr2, k):
    """
    Find the kth element from the given two sorted arrays.

    Args:
        arr1 (list): First sorted array.
        arr2 (list): Second sorted array.
        k (int): The index of the element to find.

    Returns:
        int: The kth element from the two sorted arrays.
    """
    m, n = len(arr1), len(arr2)
    if m > n:
        arr1, arr2, m, n = arr2, arr1, n, m

    left, right = 0, m

    while left <= right:
        partitionX = (left + right) // 2
        partitionY = k - partitionX

        maxLeftX = arr1[partitionX - 1] if partitionX != 0 else float('-inf')
        minRightX = arr1[partitionX] if partitionX != m else float('inf')

        maxLeftY = arr2[partitionY - 1] if partitionY != 0 else float('-inf')
        minRightY = arr2[partitionY] if partitionY != n else float('inf')

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            right = partitionX - 1
        else:
            left = partitionX + 1

    return -1

def check(candidate):
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8

check(find_kth)