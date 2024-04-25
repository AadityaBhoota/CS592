def check_min_heap_helper(arr, i):
    if not arr:
        return False
    
    for i in range(i, len(arr)//2):
        left_child = 2*i + 1
        right_child = 2*i + 2
        
        if left_child < len(arr) and arr[i] > arr[left_child]:
            return False
        
        if right_child < len(arr) and arr[i] > arr[right_child]:
            return False
    
    return True

def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)