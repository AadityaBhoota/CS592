def search(arr):
    # Check if the first element appears only once
    if arr[0] != arr[1]:
        return arr[0]

    # Check if the last element appears only once
    if arr[-1] != arr[-2]:
        return arr[-1]

    # Iterate through the array and find the element that appears only once
    for i in range(1, len(arr)-1):
        if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
            return arr[i]

# Test the function with the provided examples




def check(candidate):
    assert search([1,1,2,2,3]) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert search([1,2,2,3,3,4,4]) == 1

check(search)