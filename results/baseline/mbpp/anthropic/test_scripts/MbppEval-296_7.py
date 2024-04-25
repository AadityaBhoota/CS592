def get_Inv_Count(arr, n):
    """
    Counts the number of inversions in the given array.

    Args:
        arr (list): The input array.
        n (int): The length of the input array.

    Returns:
        int: The count of inversions in the array.
    """
    return _merge_sort(arr, 0, n - 1)

def _merge_sort(arr, left, right):
    """
    Helper function that performs merge sort and counts inversions.

    Args:
        arr (list): The input array.
        left (int): The left index of the current subarray.
        right (int): The right index of the current subarray.

    Returns:
        int: The count of inversions in the current subarray.
    """
    if left >= right:
        return 0

    mid = (left + right) // 2
    inv_count = _merge_sort(arr, left, mid)
    inv_count += _merge_sort(arr, mid + 1, right)
    inv_count += _merge(arr, left, mid, right)
    return inv_count

def _merge(arr, left, mid, right):
    """
    Helper function that merges two sorted subarrays and counts inversions.

    Args:
        arr (list): The input array.
        left (int): The left index of the current subarray.
        mid (int): The middle index of the current subarray.
        right (int): The right index of the current subarray.

    Returns:
        int: The count of inversions between the two sorted subarrays.
    """
    i = j = 0
    inv_count = 0
    temp = [0] * (right - left + 1)

    for k in range(left, right + 1):
        if i <= mid - left and j <= right - mid:
            if arr[left + i] <= arr[mid + 1 + j]:
                temp[k - left] = arr[left + i]
                i += 1
            else:
                temp[k - left] = arr[mid + 1 + j]
                j += 1
                inv_count += mid - left + 1 - i
        elif i <= mid - left:
            temp[k - left] = arr[left + i]
            i += 1
        else:
            temp[k - left] = arr[mid + 1 + j]
            j += 1

    for k in range(left, right + 1):
        arr[k] = temp[k - left]

    return inv_count

def check(candidate):
    assert get_Inv_Count([1,20,6,4,5]) == 5
    assert get_Inv_Count([1,2,1]) == 1
    assert get_Inv_Count([1,2,5,6,1]) == 3

check(get_Inv_Count)