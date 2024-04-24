def largest_subset(a):
    max_len = 0
    n = len(a)
    
    if n == 0:
        return 0
    
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if a[i] % a[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
        
        max_len = max(max_len, dp[i])
    
    return max_len

# Test cases




def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)