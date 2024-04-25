def search(arr):
    if len(arr) == 1:
        return arr[0]
    
    for i in range(0, len(arr)-1, 2):
        if arr[i] != arr[i+1]:
            return arr[i]
    
    return arr[-1]

def check(candidate):
    assert search([1,1,2,2,3]) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert search([1,2,2,3,3,4,4]) == 1

check(search)