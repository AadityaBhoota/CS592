def last(arr, x, n):
    start = 0
    end = n - 1
    result = -1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == x:
            result = mid
            start = mid + 1
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return result

# Test cases




def check(candidate):
    assert last([1,2,3],1) == 0
    assert last([1,1,1,2,3,4],1) == 2
    assert last([2,3,2,3,6,8,9],3) == 3

check(last)