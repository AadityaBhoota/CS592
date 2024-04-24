def last(arr, x, n):
    low = 0
    high = n - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            result = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return result


# Examples




def check(candidate):
    assert last([1,2,3],1) == 0
    assert last([1,1,1,2,3,4],1) == 2
    assert last([2,3,2,3,6,8,9],3) == 3

check(last)