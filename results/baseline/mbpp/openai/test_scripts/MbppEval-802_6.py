def count_rotation(arr):
    n = len(arr)
    start = 0
    end = n - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        prev = (mid + n - 1) % n
        next = (mid + 1) % n
        
        if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
            return mid
        
        if arr[start] <= arr[mid]:
            start = mid + 1
        elif arr[mid] <= arr[end]:
            end = mid - 1
    
    return 0

def check(candidate):
    assert count_rotation([3,2,1]) == 1
    assert count_rotation([4,5,1,2,3]) == 2
    assert count_rotation([7,8,9,1,2,3]) == 3
    assert count_rotation([1,2,3]) == 0
    assert count_rotation([1,3,2]) == 2

check(count_rotation)