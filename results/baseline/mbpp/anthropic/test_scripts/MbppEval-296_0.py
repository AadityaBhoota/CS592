def get_Inv_Count(arr):
    """
    Counts the number of inversions in the given array.

    Args:
    arr (list): The input array.

    Returns:
    int: The number of inversions in the input array.
    """
    return merge_sort(arr, 0, len(arr) - 1)

def merge_sort(arr, left, right):
    """
    Recursive helper function to count the number of inversions using merge sort.

    Args:
    arr (list): The input array.
    left (int): The left index of the subarray.
    right (int): The right index of the subarray.

    Returns:
    int: The number of inversions in the given subarray.
    """
    if left >= right:
        return 0

    mid = (left + right) // 2
    count = merge_sort(arr, left, mid) + merge_sort(arr, mid + 1, right)

    count += merge(arr, left, mid, right)
    return count

def merge(arr, left, mid, right):
    """
    Merges two sorted subarrays and counts the number of inversions.

    Args:
    arr (list): The input array.
    left (int): The left index of the first subarray.
    mid (int): The middle index of the first subarray.
    right (int): The right index of the second subarray.

    Returns:
    int: The number of inversions between the two subarrays.
    """
    i = left
    j = mid + 1
    count = 0

    temp = []
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            count += mid - i + 1
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for i in range(left, right + 1):
        arr[i] = temp[i - left]

    return count

def check(candidate):
    assert get_Inv_Count([1,20,6,4,5]) == 5
    assert get_Inv_Count([1,2,1]) == 1
    assert get_Inv_Count([1,2,5,6,1]) == 3

check(get_Inv_Count)