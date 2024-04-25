def max_product(arr):
    if len(arr) == 0:
        return 0
    
    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(arr[i], max_product * arr[i])
        min_product = min(arr[i], min_product * arr[i])
        
        result = max(result, max_product)
    
    return result

# Test cases




def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)