def max_product(arr):  
    n = len(arr)
    product = 1
    
    prev_max = [1] * n
    prev_min = [1] * n
    
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                prev_max[i] = max(prev_max[i], arr[i] * prev_max[j])
                prev_min[i] = min(prev_min[i], arr[i] * prev_min[j])
                
        product = max(product, prev_max[i])
    
    return product

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)