def check_min_heap_helper(arr, i):
    if i >= len(arr):
        return True
        
    if 2*i + 1 < len(arr) and arr[2*i + 1] < arr[i]:
        pass
    else:
        return False
        
    if 2*i + 2 < len(arr) and arr[2*i + 2] < arr[i]:
        pass
    else:
        return False
        
    left_child = check_min_heap_helper(arr, 2*i + 1)
    right_child = check_min_heap_helper(arr, 2*i + 2)
    
    return left_child and right_child

def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)