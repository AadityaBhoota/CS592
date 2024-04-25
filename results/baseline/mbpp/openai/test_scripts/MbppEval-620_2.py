def largest_subset(a, n):
    if len(a) == 0:
        return 0
    
    dp = [1] * len(a)
    
    for i in range(1, len(a)):
        for j in range(i):
            if a[i] % a[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)