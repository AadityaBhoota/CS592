def largest_subset(a):
    n = len(a)
    dp = [1] * n  # Initialize the dp array with 1s

    # Calculate the size of the largest subset for each element
    for i in range(1, n):
        for j in range(i):
            if a[i] % a[j] == 0 or a[j] % a[i] == 0:
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in the dp array
    return max(dp)

def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)