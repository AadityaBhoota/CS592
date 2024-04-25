def get_Inv_Count(arr):
    """
    Counts the number of inversions in an array.

    Args:
        arr (list): The input array.

    Returns:
        int: The number of inversions in the array.
    """
    return merge_sort_and_count(arr, 0, len(arr) - 1)

def merge_sort_and_count(arr, left, right):
    """
    Recursively sorts the array and counts the number of inversions.

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
    left_count = merge_sort_and_count(arr, left, mid)
    right_count = merge_sort_and_count(arr, mid + 1, right)

    return left_count + right_count + merge_and_count(arr, left, mid, right)

def merge_and_count(arr, left, mid, right):
    """
    Merges two sorted subarrays and counts the number of inversions.

    Args:
        arr (list): The input array.
        left (int): The left index of the first subarray.
        mid (int): The right index of the first subarray.
        right (int): The right index of the second subarray.

    Returns:
        int: The number of inversions between the two subarrays.
    """
    i = j = 0
    count = 0
    temp = [0] * (right - left + 1)

    for k in range(left, right + 1):
        if i > mid - left:
            temp[k - left] = arr[j + mid + 1 - left]
            j += 1
        elif j > right - mid:
            temp[k - left] = arr[i + left]
            i += 1
        elif arr[i + left] <= arr[j + mid + 1 - left]:
            temp[k - left] = arr[i + left]
            i += 1
        else:
            temp[k - left] = arr[j + mid + 1 - left]
            j += 1
            count += mid - i + 1 - left

    for k in range(left, right + 1):
        arr[k] = temp[k - left]

    return count

def check(candidate):
    assert get_Inv_Count([1,20,6,4,5]) == 5
    assert get_Inv_Count([1,2,1]) == 1
    assert get_Inv_Count([1,2,5,6,1]) == 3

check(get_Inv_Count)