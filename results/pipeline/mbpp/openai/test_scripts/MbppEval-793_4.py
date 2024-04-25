def last(arr, x, n):
    idx = -1
    for i in range(n):
        if arr[i] == x:
            idx = i
    return idx

def check(candidate):
    assert last([1,2,3],1) == 0
    assert last([1,1,1,2,3,4],1) == 2
    assert last([2,3,2,3,6,8,9],3) == 3

check(last)