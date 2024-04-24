def search(arr):
    # Base condition
    if len(arr) == 1:
        return arr[0]
    
    # Check the special cases for the first and last elements
    if arr[0] != arr[1]:
        return arr[0]
    if arr[-1] != arr[-2]:
        return arr[-1]
    
    # Perform binary search to find the element that appears only once
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]

        # Check if the left and right side of mid are evenly distributed or not
        # to decide the next move in the binary search
        if (mid - low) % 2 == 0:  # left side is even
            if arr[mid] == arr[mid-1]:
                high = mid - 2
            else:
                low = mid + 2
        else:  # right side is even
            if arr[mid] == arr[mid-1]:
                low = mid + 1
            else:
                high = mid - 1

    return None

def check(candidate):
    assert search([1,1,2,2,3]) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert search([1,2,2,3,3,4,4]) == 1

check(search)