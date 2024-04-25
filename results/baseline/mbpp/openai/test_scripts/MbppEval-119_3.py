def search(arr):
    if len(arr) == 1:
        return arr[0]
    
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if mid % 2 == 0:
            if arr[mid] == arr[mid + 1]:
                left = mid + 2
            else:
                right = mid
        else:
            if arr[mid] == arr[mid - 1]:
                left = mid + 1
            else:
                right = mid - 1

    return arr[left]

# Test cases




def check(candidate):
    assert search([1,1,2,2,3]) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert search([1,2,2,3,3,4,4]) == 1

check(search)