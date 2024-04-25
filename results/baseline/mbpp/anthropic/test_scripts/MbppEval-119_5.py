def search(arr):
    """
    Write a Python function to find the element that appears only once in a sorted array.

    Examples:
    search([1,1,2,2,3],5) == 3
    search([1,1,3,3,4,4,5,5,7,7,8],11) == 8
    search([1,2,2,3,3,4,4],7) == 1
    """
    n = len(arr)
    if n == 1:
        return arr[0]

    for i in range(0, n-1, 2):
        if arr[i] != arr[i+1]:
            return arr[i]

    return arr[-1]

def check(candidate):
    assert search([1,1,2,2,3]) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert search([1,2,2,3,3,4,4]) == 1

check(search)