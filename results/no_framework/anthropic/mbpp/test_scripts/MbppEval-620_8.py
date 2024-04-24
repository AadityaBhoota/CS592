def largest_subset(a):
    """
    Find the size of the largest subset of a list of numbers so that every pair is divisible.

    Args:
        a (list): A list of integers.

    Returns:
        int: The size of the largest subset where every pair is divisible.
    """
    n = len(a)
    dp = [1] * n  # Initialize the dynamic programming array with 1s
    
    for i in range(1, n):
        for j in range(i):
            if a[i] % a[j] == 0 or a[j] % a[i] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)