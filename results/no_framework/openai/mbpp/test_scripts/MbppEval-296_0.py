def merge_and_count_split_inv(arr, left, mid, right):
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    
    i = j = k = inv_count = 0
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[left+k] = left_arr[i]
            i += 1
        else:
            arr[left+k] = right_arr[j]
            j += 1
            inv_count += (len(left_arr) - i)
        k += 1
    
    while i < len(left_arr):
        arr[left+k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[left+k] = right_arr[j]
        j += 1
        k += 1
    
    return inv_count

def merge_sort_and_count_inv(arr, left, right):
    inv_count = 0
    
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort_and_count_inv(arr, left, mid)
        inv_count += merge_sort_and_count_inv(arr, mid+1, right)
        inv_count += merge_and_count_split_inv(arr, left, mid, right)
    
    return inv_count

def get_Inv_Count(arr):
    inv_count = merge_sort_and_count_inv(arr, 0, len(arr)-1)
    return inv_count

# Test cases




def check(candidate):
    assert get_Inv_Count([1,20,6,4,5]) == 5
    assert get_Inv_Count([1,2,1]) == 1
    assert get_Inv_Count([1,2,5,6,1]) == 3

check(get_Inv_Count)