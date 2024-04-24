def search(arr, n):
    low = 0
    high = n - 1

    while low <= high:
        if low == high:
            return arr[low]

        mid = low + (high - low) // 2

        if mid % 2 == 0:
            if arr[mid] == arr[mid + 1]:
                low = mid + 2
            else:
                high = mid
        else:
            if arr[mid] == arr[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1

# Examples




def check(candidate):
    assert search([1,1,2,2,3]) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert search([1,2,2,3,3,4,4]) == 1

check(search)