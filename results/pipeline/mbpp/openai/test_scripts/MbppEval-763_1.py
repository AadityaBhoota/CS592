def find_min_diff(arr, n): 
    arr.sort()  # Step 1: Sorting the array in non-decreasing order
    
    min_diff = float('inf')  # Step 2: Initializing min_diff as a large value
    
    # Step 3: Calculating and updating min_diff
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        if diff < min_diff:
            min_diff = diff

    return min_diff

def check(candidate):
    assert find_min_diff((1,5,3,19,18,25),6) == 1
    assert find_min_diff((4,3,2,6),4) == 1
    assert find_min_diff((30,5,20,9),4) == 4

check(find_min_diff)