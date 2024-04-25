def search(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if mid > 0 and arr[mid] == arr[mid - 1]:
            left = mid + 1
        elif mid < len(arr) - 1 and arr[mid] == arr[mid + 1]:
            right = mid - 1
        else:
            return arr[mid]

    return -1

def check(candidate):
    assert search([1,1,2,2,3]) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert search([1,2,2,3,3,4,4]) == 1

check(search)