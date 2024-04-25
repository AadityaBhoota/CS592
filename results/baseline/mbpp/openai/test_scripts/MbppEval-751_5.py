def check_min_heap_helper(arr, i):
    n = len(arr)
    
    if i >= n:
        return True
    
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] < arr[i]:
        return False
    if right < n and arr[right] < arr[i]:
        return False

    return check_min_heap_helper(arr, left) and check_min_heap_helper(arr, right)

def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)