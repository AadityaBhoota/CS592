def get_Inv_Count(arr):
    return merge_sort(arr, len(arr))

def merge_sort(arr, n):
    if n == 1:
        return 0

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    left_inversions = merge_sort(left, mid)
    right_inversions = merge_sort(right, n - mid)

    i = j = 0
    inversions = 0
    for k in range(n):
        if i < mid and (j >= n - mid or left[i] <= right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            inversions += mid - i

    return left_inversions + right_inversions + inversions

def check(candidate):
    assert get_Inv_Count([1,20,6,4,5]) == 5
    assert get_Inv_Count([1,2,1]) == 1
    assert get_Inv_Count([1,2,5,6,1]) == 3

check(get_Inv_Count)