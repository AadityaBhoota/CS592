def get_Inv_Count(arr):
    """
    Counts the number of inversions in the given array.

    Args:
        arr (list): The input array.

    Returns:
        int: The number of inversions in the array.
    """
    return merge_sort(arr, 0, len(arr) - 1)

def merge_sort(arr, left, right):
    """
    Performs the merge sort algorithm and counts the number of inversions.

    Args:
        arr (list): The input array.
        left (int): The left index of the subarray.
        right (int): The right index of the subarray.

    Returns:
        int: The number of inversions in the subarray.
    """
    if left >= right:
        return 0

    mid = (left + right) // 2
    inv_count = merge_sort(arr, left, mid)
    inv_count += merge_sort(arr, mid + 1, right)
    inv_count += merge(arr, left, mid, right)
    return inv_count

def merge(arr, left, mid, right):
    """
    Merges two sorted subarrays and counts the number of inversions.

    Args:
        arr (list): The input array.
        left (int): The left index of the first subarray.
        mid (int): The middle index of the subarrays.
        right (int): The right index of the second subarray.

    Returns:
        int: The number of inversions between the two subarrays.
    """
    i, j = left, mid + 1
    inv_count = 0
    temp = [0] * (right - left + 1)
    k = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += mid - i + 1
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(right - left + 1):
        arr[left + i] = temp[i]

    return inv_count

def check(candidate):
    assert get_Inv_Count([1,20,6,4,5]) == 5
    assert get_Inv_Count([1,2,1]) == 1
    assert get_Inv_Count([1,2,5,6,1]) == 3

check(get_Inv_Count)