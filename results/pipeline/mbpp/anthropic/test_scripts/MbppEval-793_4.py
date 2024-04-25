def last(arr, x, n):
    left = 0
    right = n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == x:
            left = mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    if left == 0:
        return -1
    else:
        return left - 1

def check(candidate):
    assert last([1,2,3],1) == 0
    assert last([1,1,1,2,3,4],1) == 2
    assert last([2,3,2,3,6,8,9],3) == 3

check(last)