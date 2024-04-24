def find_min_diff(arr, n):
    """
    Find the minimum difference between any two elements in a given array.
    
    Args:
        arr (list): The input array.
        n (int): The length of the array.
    
    Returns:
        int: The minimum difference between any two elements in the array.
    """
    # Sort the array
    arr.sort()
    
    # Initialize the minimum difference
    min_diff = float('inf')
    
    # Iterate through the array and find the minimum difference
    for i in range(1, n):
        diff = abs(arr[i] - arr[i-1])
        min_diff = min(min_diff, diff)
    
    return min_diff

def check(candidate):
    assert find_min_diff((1,5,3,19,18,25),6) == 1
    assert find_min_diff((4,3,2,6),4) == 1
    assert find_min_diff((30,5,20,9),4) == 4

check(find_min_diff)