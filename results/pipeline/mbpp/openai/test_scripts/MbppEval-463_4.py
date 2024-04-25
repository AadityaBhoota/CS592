def max_subarray_product(arr):
    if not arr:
        return None
    
    current_max_product = current_min_product = result = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < 0:
            current_max_product, current_min_product = current_min_product, current_max_product
        
        current_max_product = max(arr[i], current_max_product * arr[i])
        current_min_product = min(arr[i], current_min_product * arr[i])
        
        result = max(result, current_max_product)
    
    return result

def check(candidate):
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([6, -3, -10, 0, 2]) == 180
    assert max_subarray_product([-2, -40, 0, -2, -3]) == 80

check(max_subarray_product)