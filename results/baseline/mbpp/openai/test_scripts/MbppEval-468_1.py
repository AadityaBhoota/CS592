def max_product(arr):
    if len(arr) == 0:
        return 0
    
    dp = [0] * len(arr)
    result = 0
    
    for i in range(len(arr)):
        maximum = 0
        for j in range(i):
            if arr[i] > arr[j]:
                product = arr[i] * dp[j]
                maximum = max(maximum, product)
        
        if maximum == 0:
            dp[i] = arr[i]
        else:
            dp[i] = maximum
        
        result = max(result, dp[i])
    
    return result

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)