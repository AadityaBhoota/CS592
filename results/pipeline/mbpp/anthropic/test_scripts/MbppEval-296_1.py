def get_Inv_Count(arr):
    return merge_sort(arr, 0, len(arr) - 1)

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        left_count = merge_sort(arr, left, mid)
        right_count = merge_sort(arr, mid + 1, right)
        return left_count + right_count + merge(arr, left, mid, right)
    return 0

def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    count = 0
    temp = [0] * (right - left + 1)
    k = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            count += mid - i + 1
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

    for i in range(left, right + 1):
        arr[i] = temp[i - left]

    return count

def check(candidate):
    assert get_Inv_Count([1,20,6,4,5]) == 5
    assert get_Inv_Count([1,2,1]) == 1
    assert get_Inv_Count([1,2,5,6,1]) == 3

check(get_Inv_Count)