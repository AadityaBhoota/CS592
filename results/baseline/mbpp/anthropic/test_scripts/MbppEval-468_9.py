def max_product(arr):
    n = len(arr)
    if n < 2:
        return 0
    
    # Initialize the DP arrays
    dp_len = [1] * n
    dp_product = [arr[0]] * n
    
    # Iterate through the array and compute the maximum length and product of increasing subsequences
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                if dp_len[j] + 1 > dp_len[i]:
                    dp_len[i] = dp_len[j] + 1
                    dp_product[i] = dp_product[j] * arr[i]
    
    # Find the maximum product
    max_len = max(dp_len)
    return max(dp_product[i] for i in range(n) if dp_len[i] == max_len)

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)