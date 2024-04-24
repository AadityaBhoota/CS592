def get_Inv_Count(arr, n):
    """
    Function to count the number of inversions in the given array.

    Args:
        arr (list): The input array.
        n (int): The length of the input array.

    Returns:
        int: The number of inversions in the array.
    """
    return merge_sort(arr, 0, n - 1)

def merge_sort(arr, left, right):
    """
    Recursive function to perform merge sort and count the number of inversions.

    Args:
        arr (list): The input array.
        left (int): The left index of the current subarray.
        right (int): The right index of the current subarray.

    Returns:
        int: The number of inversions in the current subarray.
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
    Helper function to merge two sorted subarrays and count the number of inversions.

    Args:
        arr (list): The input array.
        left (int): The left index of the current subarray.
        mid (int): The middle index of the current subarray.
        right (int): The right index of the current subarray.

    Returns:
        int: The number of inversions in the current subarray.
    """
    i, j = left, mid + 1
    inv_count = 0
    temp = []

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            inv_count += mid - i + 1
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for i in range(left, right + 1):
        arr[i] = temp[i - left]

    return inv_count

def check(candidate):
    assert get_Inv_Count([1,20,6,4,5]) == 5
    assert get_Inv_Count([1,2,1]) == 1
    assert get_Inv_Count([1,2,5,6,1]) == 3

check(get_Inv_Count)