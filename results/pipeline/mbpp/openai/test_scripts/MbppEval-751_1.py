def check_min_heap_helper(arr, i):
    left_child_index = 2*i + 1
    right_child_index = 2*i + 2
    
    if left_child_index < len(arr) and not check_min_heap_helper(arr, left_child_index):
        return False
    
    if right_child_index < len(arr) and not check_min_heap_helper(arr, right_child_index):
        return False
    
    if left_child_index < len(arr) and arr[left_child_index] < arr[i]:
        return False
    
    if right_child_index < len(arr) and arr[right_child_index] < arr[i]:
        return False
    
    return True

def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)