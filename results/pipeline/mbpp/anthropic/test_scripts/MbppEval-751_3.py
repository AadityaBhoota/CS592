def check_min_heap_helper(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check if the current node is smaller than its left and right children
    if left < len(arr) and arr[i] > arr[left]:
        return False
    if right < len(arr) and arr[i] > arr[right]:
        return False
    
    # Recursively check the left and right subtrees
    if left < len(arr):
        if not check_min_heap_helper(arr, left):
            return False
    if right < len(arr):
        if not check_min_heap_helper(arr, right):
            return False
    
    return True

def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)