def kth_element(arr, k):
    """
    Write a function to find the kth element in the given array using 1-based indexing.

    Examples:
    kth_element([12,3,5,7,19], 5, 2) == 3
    kth_element([17,24,8,23], 4, 3) == 8
    kth_element([16,21,25,36,4], 5, 4) == 36
    """
    if not arr or k < 1 or k > len(arr):
        return None

    return _quickselect(arr, 0, len(arr) - 1, k - 1)


def _quickselect(arr, left, right, k):
    """
    Helper function to find the kth smallest element using the quick-select algorithm.
    """
    pivot = arr[right]
    i = left

    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]

    if i == k:
        return arr[i]
    elif i > k:
        return _quickselect(arr, left, i - 1, k)
    else:
        return _quickselect(arr, i + 1, right, k)

def check(candidate):
    assert kth_element([12,3,5,7,19], 2) == 3
    assert kth_element([17,24,8,23], 3) == 8
    assert kth_element([16,21,25,36,4], 4) == 36

check(kth_element)