def search(arr, n):
    if n == 1:
        return arr[0]

    start, end = 0, n - 1

    while start <= end:
        mid = start + (end - start) // 2

        if mid > 0 and arr[mid] == arr[mid - 1]:
            if mid % 2 == 0:
                start = mid + 1
            else:
                end = mid - 1
        elif mid < n - 1 and arr[mid] == arr[mid + 1]:
            if mid % 2 == 0:
                end = mid - 1
            else:
                start = mid + 1
        else:
            return arr[mid]

# Test cases




def check(candidate):
    assert search([1,1,2,2,3]) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert search([1,2,2,3,3,4,4]) == 1

check(search)