def last(arr, x):
    last_pos = -1
    
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == x:
            last_pos = i
            break

    return last_pos

def check(candidate):
    assert last([1,2,3],1) == 0
    assert last([1,1,1,2,3,4],1) == 2
    assert last([2,3,2,3,6,8,9],3) == 3

check(last)