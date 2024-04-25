def find_min_diff(arr, n):
    # Sort the array in ascending order
    arr.sort()
    
    # Initialize min_diff to a large value
    min_diff = float('inf')
    
    # Iterate through the sorted array and calculate the difference
    for i in range(1, n):
        diff = abs(arr[i] - arr[i-1])
        min_diff = min(min_diff, diff)
    
    return min_diff

def check(candidate):
    assert find_min_diff((1,5,3,19,18,25),6) == 1
    assert find_min_diff((4,3,2,6),4) == 1
    assert find_min_diff((30,5,20,9),4) == 4

check(find_min_diff)