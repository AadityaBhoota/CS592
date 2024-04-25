def max_sum(arr): 
    inc_sum = [0] * len(arr)
    dec_sum = [0] * len(arr)
    
    # Calculate the maximum increasing subsequence sum ending at each index
    for i in range(len(arr)):
        inc_sum[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                inc_sum[i] = max(inc_sum[i], inc_sum[j] + arr[i])
    
    # Calculate the maximum decreasing subsequence sum starting at each index
    for i in range(len(arr) - 1, -1, -1):
        dec_sum[i] = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                dec_sum[i] = max(dec_sum[i], dec_sum[j] + arr[i])
    
    max_sum_bitonic = 0
    for i in range(len(arr)):
        max_sum_bitonic = max(max_sum_bitonic, inc_sum[i] + dec_sum[i] - arr[i])
    
    return max_sum_bitonic

def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)