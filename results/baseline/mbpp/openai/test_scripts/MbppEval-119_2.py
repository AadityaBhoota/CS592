def search(arr):
    # Handle edge cases
    if len(arr) == 1:
        return arr[0]

    # Initialize variables
    left = 0
    right = len(arr) - 1
  
    # Perform binary search
    while left < right:
        mid = left + (right - left) // 2
        
        # Check if the element at mid is the unique element
        if mid % 2 == 0:
            if arr[mid] != arr[mid + 1]:
                right = mid
            else:
                left = mid + 2
        else:
            if arr[mid] != arr[mid - 1]:
                right = mid - 1
            else:
                left = mid + 1
                
    return arr[left]
    
# Test cases




def check(candidate):
    assert search([1,1,2,2,3]) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert search([1,2,2,3,3,4,4]) == 1

check(search)