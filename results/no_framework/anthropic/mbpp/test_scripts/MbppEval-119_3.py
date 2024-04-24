def search(arr):
    """
    Write a python function to find the element that appears only once in a sorted array.

    Examples:
    search([1,1,2,2,3],5) == 3
    search([1,1,3,3,4,4,5,5,7,7,8],11) == 8
    search([1,2,2,3,3,4,4],7) == 1
    """
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if mid % 2 == 1:
            mid -= 1

        if arr[mid] == arr[mid + 1]:
            left = mid + 2
        else:
            right = mid

    return arr[left]

def check(candidate):
    assert search([1,1,2,2,3]) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert search([1,2,2,3,3,4,4]) == 1

check(search)