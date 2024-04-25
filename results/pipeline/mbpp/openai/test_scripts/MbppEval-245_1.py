def max_sum(arr): 
    n = len(arr)
    
    inc_sum = [0] * n
    dec_sum = [0] * n
    
    for i in range(n):
        inc_sum[i] = arr[i]
        dec_sum[i] = arr[i]
        
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                inc_sum[i] = max(inc_sum[i], inc_sum[j] + arr[i])
    
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if arr[i] > arr[j]:
                dec_sum[i] = max(dec_sum[i], dec_sum[j] + arr[i])
    
    max_bitonic_sum = 0
    for i in range(n):
        max_bitonic_sum = max(max_bitonic_sum, inc_sum[i] + dec_sum[i] - arr[i])
    
    return max_bitonic_sum

def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)