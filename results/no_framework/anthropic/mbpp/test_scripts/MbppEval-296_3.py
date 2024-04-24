def get_Inv_Count(arr):
    """
    Write a python function to count inversions in an array.

    Examples:
    get_Inv_Count([1,20,6,4,5],5) == 5
    get_Inv_Count([1,2,1],3) == 1
    get_Inv_Count([1,2,5,6,1],5) == 3
    """
    return merge_sort(arr, 0, len(arr) - 1)[1]

def merge_sort(arr, left, right):
    if left >= right:
        return arr, 0

    mid = (left + right) // 2
    left_arr, left_count = merge_sort(arr, left, mid)
    right_arr, right_count = merge_sort(arr, mid + 1, right)

    merged_arr, merge_count = merge(left_arr, right_arr)
    return merged_arr, left_count + right_count + merge_count

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    count = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
            count += len(left) - left_index

    result += left[left_index:]
    result += right[right_index:]
    return result, count

def check(candidate):
    assert get_Inv_Count([1,20,6,4,5]) == 5
    assert get_Inv_Count([1,2,1]) == 1
    assert get_Inv_Count([1,2,5,6,1]) == 3

check(get_Inv_Count)