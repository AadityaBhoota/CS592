def max_product(arr):
    arr = sorted(arr)
    max_product = 1
    current_product = 1
    
    for num in arr:
        current_product = max(current_product * num, num)
        max_product = max(max_product, current_product)

    return max_product

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)