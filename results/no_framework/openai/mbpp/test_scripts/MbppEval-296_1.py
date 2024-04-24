def merge_and_count(arr, left, mid, right):
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    
    inv_count = 0
    i = 0
    j = 0
    k = left
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
            inv_count += (mid - (left + i) + 1)
        k += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    
    return inv_count

def merge_sort(arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort(arr, left, mid)
        inv_count += merge_sort(arr, mid+1, right)
        inv_count += merge_and_count(arr, left, mid, right)
    
    return inv_count

def get_Inv_Count(arr): 
    return merge_sort(arr, 0, len(arr)-1)

# Test cases




def check(candidate):
    assert get_Inv_Count([1,20,6,4,5]) == 5
    assert get_Inv_Count([1,2,1]) == 1
    assert get_Inv_Count([1,2,5,6,1]) == 3

check(get_Inv_Count)