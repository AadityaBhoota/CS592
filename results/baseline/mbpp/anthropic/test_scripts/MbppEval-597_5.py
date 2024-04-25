def find_kth(arr1, arr2, k):
    """
    Find the kth element from the given two sorted arrays.

    Args:
        arr1 (list): First sorted array.
        arr2 (list): Second sorted array.
        k (int): The index of the element to be found.

    Returns:
        int: The kth element from the combined sorted arrays.
    """
    if not arr1:
        return arr2[k - 1]
    if not arr2:
        return arr1[k - 1]

    if k == 1:
        return min(arr1[0], arr2[0])

    i = min(len(arr1), k // 2)
    j = min(len(arr2), k // 2)

    if arr1[i - 1] > arr2[j - 1]:
        return find_kth(arr1, arr2[j:], k - j)
    else:
        return find_kth(arr1[i:], arr2, k - i)

def check(candidate):
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8

check(find_kth)