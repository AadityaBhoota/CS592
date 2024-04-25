def search(arr):
    for i in range(0, len(arr), 2):
        if i == len(arr) - 1 or arr[i] != arr[i+1]:
            return arr[i]

# Test cases




def check(candidate):
    assert search([1,1,2,2,3]) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert search([1,2,2,3,3,4,4]) == 1

check(search)