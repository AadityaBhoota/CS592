def merge_sort(arr, n):
    if n == 1:
        return arr, 0
    
    mid = n // 2
    left, left_inv = merge_sort(arr[:mid], mid)
    right, right_inv = merge_sort(arr[mid:], n - mid)
    
    merged = []
    i, j = 0, 0
    inversions = left_inv + right_inv
    
    while i < mid and j < n - mid:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += mid - i
    
    merged += left[i:]
    merged += right[j:]
    
    return merged, inversions

def get_Inv_Count(arr, n):
    _, inversions = merge_sort(arr, n)
    return inversions

def check(candidate):
    assert get_Inv_Count([1,20,6,4,5]) == 5
    assert get_Inv_Count([1,2,1]) == 1
    assert get_Inv_Count([1,2,5,6,1]) == 3

check(get_Inv_Count)