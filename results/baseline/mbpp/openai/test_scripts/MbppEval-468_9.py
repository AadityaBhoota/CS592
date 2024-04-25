def max_product(arr):   
    n = len(arr)
    max_prod = 0

    for i in range(1 << n):
        subseq = []
        for j in range(n):
            if i & (1 << j):
                subseq.append(arr[j])
        if subseq == sorted(subseq):
            product = 1
            for num in subseq:
                product *= num
            max_prod = max(max_prod, product)

    return max_prod

# Test cases




def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)