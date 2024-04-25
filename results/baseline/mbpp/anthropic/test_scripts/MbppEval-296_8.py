def get_Inv_Count(arr):
    """
    Write a Python function to count inversions in an array.

    Examples:
    get_Inv_Count([1, 20, 6, 4, 5], 5) == 5
    get_Inv_Count([1, 2, 1], 3) == 1
    get_Inv_Count([1, 2, 5, 6, 1], 5) == 3
    """
    return merge_sort(arr, 0, len(arr) - 1)

def merge_sort(arr, left, right):
    """
    Helper function to perform merge sort and count inversions.
    """
    if left < right:
        mid = (left + right) // 2
        left_count = merge_sort(arr, left, mid)
        right_count = merge_sort(arr, mid + 1, right)
        inversion_count = merge_and_count_inversions(arr, left, mid, right)
        return left_count + right_count + inversion_count
    return 0

def merge_and_count_inversions(arr, left, mid, right):
    """
    Helper function to merge two sorted subarrays and count inversions.
    """
    i = j = 0
    inversion_count = 0
    left_subarray = arr[left:mid + 1]
    right_subarray = arr[mid + 1:right + 1]

    for k in range(left, right + 1):
        if i < len(left_subarray) and j < len(right_subarray):
            if left_subarray[i] <= right_subarray[j]:
                arr[k] = left_subarray[i]
                i += 1
            else:
                arr[k] = right_subarray[j]
                j += 1
                inversion_count += len(left_subarray) - i
        elif i < len(left_subarray):
            arr[k] = left_subarray[i]
            i += 1
        else:
            arr[k] = right_subarray[j]
            j += 1

    return inversion_count

def check(candidate):
    assert get_Inv_Count([1,20,6,4,5]) == 5
    assert get_Inv_Count([1,2,1]) == 1
    assert get_Inv_Count([1,2,5,6,1]) == 3

check(get_Inv_Count)