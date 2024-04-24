def max_product(arr):
    n = len(arr)
    max_product = 1
    result = 1
    
    i = 0
    while i < n:
        j = i + 1
        while j < n and arr[j] > arr[j - 1]:
            j += 1
        temp_max = 0
        
        for k in range(i, j):
            temp_product = arr[k]
            for l in range(i, j):
                if l != k:
                    temp_product *= arr[l]
            if temp_product > temp_max:
                temp_max = temp_product
        
        if temp_max > max_product:
            max_product = temp_max
        
        i = j
    
    return max_product

# Test cases




def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)