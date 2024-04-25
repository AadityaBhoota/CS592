def merge_and_count(arr, n):
    if n <= 1:
        return 0

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    left_count = merge_and_count(left, mid)
    right_count = merge_and_count(right, n - mid)

    i = j = 0
    inv_count = 0
    for k in range(n):
        if i < mid and (j >= n - mid or left[i] <= right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            inv_count += (mid - i)

    return left_count + right_count + inv_count

def get_Inv_Count(arr, n):
    return merge_and_count(arr, n)

def check(candidate):
    assert get_Inv_Count([1,20,6,4,5]) == 5
    assert get_Inv_Count([1,2,1]) == 1
    assert get_Inv_Count([1,2,5,6,1]) == 3

check(get_Inv_Count)