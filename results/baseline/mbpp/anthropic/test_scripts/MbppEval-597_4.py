def find_kth(arr1, arr2, k):
    """
    Find the kth element from the two given sorted arrays.

    Args:
        arr1 (list): The first sorted array.
        arr2 (list): The second sorted array.
        k (int): The index of the element to be found (1-based indexing).

    Returns:
        int: The kth element from the two sorted arrays.
    """
    n, m = len(arr1), len(arr2)
    left, right = 0, n

    while left <= right:
        partitionX = (left + right) // 2
        partitionY = k - partitionX

        # Ensure partitionX is within the bounds of arr1
        partitionX = max(partitionX, 0)
        partitionX = min(partitionX, n)

        # Ensure partitionY is within the bounds of arr2
        partitionY = max(partitionY, 0)
        partitionY = min(partitionY, m)

        # Get the max of left partition elements
        maxLeftX = arr1[partitionX - 1] if partitionX != 0 else float('-inf')
        maxLeftY = arr2[partitionY - 1] if partitionY != 0 else float('-inf')

        # Get the min of right partition elements
        minRightX = arr1[partitionX] if partitionX != n else float('inf')
        minRightY = arr2[partitionY] if partitionY != m else float('inf')

        # If we have found the element
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            right = partitionX - 1
        else:
            left = partitionX + 1

    # If element is not found
    return -1

def check(candidate):
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8

check(find_kth)