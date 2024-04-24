def max_sum_increasing_subseq(a, n, i, k):
    # Base case: if the given index i is greater than or equal to the given k,
    # the maximum sum is simply the value at the kth index.
    if i >= k:
        return a[k]

    # Initialize the dp array with the values from the given array a.
    dp = a[:]

    # Iterate through the array from the beginning to the index i.
    for j in range(i):
        # If the current element is less than the element at index i,
        # update the dp value at index i to the maximum of the current dp value
        # and the sum of the current element and the maximum sum of the
        # increasing subsequence up to the jth index.
        if a[j] < a[i]:
            dp[i] = max(dp[i], a[i] + dp[j])

    # Find the maximum sum of increasing subsequence including the kth element.
    max_sum = 0
    for j in range(i + 1, k + 1):
        max_sum = max(max_sum, dp[j])

    return max_sum

def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)