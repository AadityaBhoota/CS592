def max_sum_increasing_subseq(a, n, index, k):
    dp = [0] * n
    max_sum = 0

    # Base case
    if index == 0:
        return a[0]

    # Iterate through the array
    for i in range(n):
        # Find the maximum sum of increasing subsequence up to index i
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + a[i])

        # Update the max_sum if i is less than k
        if i < k:
            max_sum = max(max_sum, dp[i])

    return max_sum

def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)