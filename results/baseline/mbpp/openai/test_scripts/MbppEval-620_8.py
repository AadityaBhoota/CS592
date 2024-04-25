def largest_subset(a):
    max_subset = 0
    a.sort()
    n = len(a)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if a[i] % a[j] == 0 and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
        max_subset = max(max_subset, dp[i])
    
    return max_subset

# Test cases




def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)