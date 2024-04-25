def count_rotation(arr, n):
    low = 0
    high = n - 1
    
    while low < high:
        mid = (low + high) // 2
        
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    
    return high

def check(candidate):
    assert count_rotation([3,2,1]) == 1
    assert count_rotation([4,5,1,2,3]) == 2
    assert count_rotation([7,8,9,1,2,3]) == 3
    assert count_rotation([1,2,3]) == 0
    assert count_rotation([1,3,2]) == 2

check(count_rotation)