def last(arr, x):
    last_index = -1
    for i in range(len(arr)):
        if arr[i] == x:
            last_index = i
    return last_index

def check(candidate):
    assert last([1,2,3],1) == 0
    assert last([1,1,1,2,3,4],1) == 2
    assert last([2,3,2,3,6,8,9],3) == 3

check(last)