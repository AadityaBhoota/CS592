def max_product(arr):
    n = len(arr)
    arr.sort()
    max_product = 1

    for i in range(n):
        product = 1
        for j in range(i+1):
            product *= arr[j]
        max_product = max(max_product, product)

    return max_product

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)