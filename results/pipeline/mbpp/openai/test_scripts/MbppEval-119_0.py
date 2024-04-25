def search(arr):
    unique_element = None
    n = len(arr)
    
    for i in range(0, n, 2):
        if i == n - 1 or arr[i] != arr[i + 1]:
            unique_element = arr[i]
            break
    
    return unique_element

def check(candidate):
    assert search([1,1,2,2,3]) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert search([1,2,2,3,3,4,4]) == 1

check(search)