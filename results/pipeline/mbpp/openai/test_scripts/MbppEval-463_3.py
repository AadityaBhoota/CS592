def max_subarray_product(arr):
    if not arr:
        return None
    
    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]
    
    for i in range(1, len(arr)):
        temp_max = max(arr[i], max_product * arr[i], min_product * arr[i])
        temp_min = min(arr[i], max_product * arr[i], min_product * arr[i])
        
        max_product = temp_max
        min_product = temp_min
        
        result = max(result, max_product)
        
    return result

def check(candidate):
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([6, -3, -10, 0, 2]) == 180
    assert max_subarray_product([-2, -40, 0, -2, -3]) == 80

check(max_subarray_product)