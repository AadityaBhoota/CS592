def search(arr):
    # Check if the array is empty
    if not arr:
        return None
    
    for i in range(0, len(arr), 2):
        # Check if the next element is out of bounds or current element is not equal to next element
        if i == len(arr)-1 or arr[i] != arr[i+1]:
            return arr[i]

def check(candidate):
    assert search([1,1,2,2,3]) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert search([1,2,2,3,3,4,4]) == 1

check(search)