def max_subarray_product(arr):
    if not arr:
        return 0
    
    max_ending_here = arr[0]
    min_ending_here = arr[0]
    max_so_far = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_ending_here, min_ending_here = min_ending_here, max_ending_here
        
        max_ending_here = max(arr[i], max_ending_here * arr[i])
        min_ending_here = min(arr[i], min_ending_here * arr[i])
        
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

# Test cases




def check(candidate):
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([6, -3, -10, 0, 2]) == 180
    assert max_subarray_product([-2, -40, 0, -2, -3]) == 80

check(max_subarray_product)