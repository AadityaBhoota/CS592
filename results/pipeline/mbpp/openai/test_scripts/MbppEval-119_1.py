def search(arr):
    if len(arr) == 1:
        return arr[0]

    start, end = 0, len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        elif mid % 2 == 0 and arr[mid] == arr[mid + 1]:
            start = mid + 2
        else:
            end = mid

def check(candidate):
    assert search([1,1,2,2,3]) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert search([1,2,2,3,3,4,4]) == 1

check(search)