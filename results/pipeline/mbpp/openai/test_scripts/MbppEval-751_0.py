def check_min_heap_helper(arr, i):
    if i >= len(arr):
        return True
    
    left = 2*i + 1
    if left >= len(arr):
        return True
    
    right = 2*i + 2
    if right >= len(arr):
        return True
    
    left_child_valid = check_min_heap_helper(arr, left)
    right_child_valid = check_min_heap_helper(arr, right)
    
    if not left_child_valid or not right_child_valid:
        return False
    
    if arr[i] > arr[left] or (right < len(arr) and arr[i] > arr[right]):
        return False
    
    return True

def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)