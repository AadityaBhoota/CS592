def search(arr):
    low = 0
    high = len(arr) - 1
    
    while low < high:
        mid = (low + high) // 2
        if (mid % 2 == 0 and arr[mid] == arr[mid+1]) or \
           (mid % 2 == 1 and arr[mid] == arr[mid-1]):
            low = mid + 1
        else:
            high = mid
    
    return arr[low]

def check(candidate):
    assert search([1,1,2,2,3]) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert search([1,2,2,3,3,4,4]) == 1

check(search)