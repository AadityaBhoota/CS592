def max_product(arr):   
    arr.sort()
    
    max_prod = 1

    for num in arr:
        max_prod *= num

    increasing_subsequence = []
    for num in arr:
        if not increasing_subsequence or num > increasing_subsequence[-1]:
            increasing_subsequence.append(num)

    temp_prod = 1
    for num in increasing_subsequence:
        temp_prod *= num
        max_prod = max(max_prod, temp_prod)

    return max_prod

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)