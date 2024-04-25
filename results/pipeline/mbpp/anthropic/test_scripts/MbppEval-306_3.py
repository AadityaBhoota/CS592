def max_sum_increasing_subseq(a, n, index, k):
    dp = [0] * n
    
    # Initialize the first element
    dp[0] = a[0]
    
    # Iterate through the array
    for i in range(1, n):
        # Find the maximum sum of the increasing subsequence up to i, including any element after i up to the kth element
        if i <= index:
            dp[i] = max(dp[i-1], a[i])
        elif a[i] < a[k]:
            dp[k] = max(dp[k], dp[i-1] + a[i])
        else:
            dp[i] = dp[i-1]
    
    # Return the maximum value in the dp array
    return dp[k]

def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)