def max_subarray_product(arr):
    if not arr:
        return 0
    
    max_prod = arr[0]
    curr_max = arr[0]
    curr_min = arr[0]
    
    for num in arr[1:]:
        if num < 0:
            curr_max, curr_min = curr_min, curr_max
        
        curr_max = max(num, curr_max * num)
        curr_min = min(num, curr_min * num)
        
        max_prod = max(max_prod, curr_max)
    
    return max_prod

# Test cases




def check(candidate):
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([6, -3, -10, 0, 2]) == 180
    assert max_subarray_product([-2, -40, 0, -2, -3]) == 80

check(max_subarray_product)