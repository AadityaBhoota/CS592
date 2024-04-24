def search(arr):
    """
    Write a python function to find the element that appears only once in a sorted array.

    Examples:
    search([1,1,2,2,3],5) == 3
    search([1,1,3,3,4,4,5,5,7,7,8],11) == 8
    search([1,2,2,3,3,4,4],7) == 1
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if mid == 0 or mid == len(arr) - 1:
            return arr[mid]

        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]

        if arr[mid] == arr[mid - 1]:
            if (mid - left) % 2 == 0:
                left = mid + 1
            else:
                right = mid - 2
        else:
            if (right - mid) % 2 == 0:
                right = mid - 1
            else:
                left = mid + 2

    return -1  # no unique element found

def check(candidate):
    assert search([1,1,2,2,3]) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert search([1,2,2,3,3,4,4]) == 1

check(search)