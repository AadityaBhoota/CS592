def max_product(arr):
    if len(arr) == 0:
        return 0
    
    max_prod = arr[0]
    curr_prod = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            curr_prod *= arr[i]
            max_prod = max(max_prod, curr_prod)
        else:
            curr_prod = arr[i]
    
    return max_prod

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)