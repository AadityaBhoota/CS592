def max_sum(arr): 
    n = len(arr) 
    if n == 0: 
        return 0
    
    # Initialize two arrays to store the maximum increasing subsequence from left and right respectively
    inc = [0] * n
    dec = [0] * n
    
    # Calculate the maximum increasing subsequence ending at each index
    for i in range(n):
        inc[i] = arr[i]
        for j in range(i):
            if arr[j] < arr[i]:
                inc[i] = max(inc[i], inc[j] + arr[i])
    
    # Calculate the maximum decreasing subsequence starting from each index
    for i in range(n-1, -1, -1):
        dec[i] = arr[i]
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                dec[i] = max(dec[i], dec[j] + arr[i])

    # Compute the maximum sum of bitonic subsequence by finding the maximum sum for each index
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i] - arr[i])
    
    return max_sum

# Test cases




def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)