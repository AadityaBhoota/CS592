def max_product(arr, n):
    if len(arr) < n:
        return "Invalid input"
    
    arr.sort()
    
    max_prod = 1
    for i in range(len(arr) - n, len(arr)):
        max_prod *= arr[i]
    
    return max_prod

# Test cases




def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)