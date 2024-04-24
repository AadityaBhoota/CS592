def get_median(arr1, arr2, n):
    """
    Find the median of two sorted lists of the same size.

    Args:
        arr1 (list): First sorted list.
        arr2 (list): Second sorted list.
        n (int): Size of the lists.

    Returns:
        float: Median of the two sorted lists.
    """
    left = 0
    right = n - 1
    
    while True:
        if left == n - 1:
            return (arr1[left] + arr2[0]) / 2
        
        if left == n - 2:
            return (max(arr1[left], arr2[left]) + min(arr1[left+1], arr2[left+1])) / 2
        
        mid1 = (left + right) // 2
        mid2 = mid1 + 1
        
        if arr1[mid1] <= arr2[mid1] and arr1[mid2] >= arr2[mid2]:
            return (max(arr1[mid1], arr2[mid1]) + min(arr1[mid2], arr2[mid2])) / 2
        
        if arr1[mid1] > arr2[mid1]:
            right = mid1 - 1
        else:
            left = mid1 + 1

def check(candidate):
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0

check(get_median)