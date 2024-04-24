def max_product(arr):
    """
    Finds the maximum product formed by multiplying numbers of an increasing subsequence of the given array.

    Args:
        arr (list): The input array.

    Returns:
        int: The maximum product.
    """
    n = len(arr)
    if n < 2:
        return 0

    # Create a DP array to store the maximum product ending at each index
    dp = [0] * n

    # Initialize the first element of the DP array
    dp[0] = arr[0]

    # Compute the maximum product for each index
    for i in range(1, n):
        max_product = 0
        for j in range(i):
            if arr[i] > arr[j]:
                max_product = max(max_product, dp[j] * arr[i])
        dp[i] = max(dp[i - 1], max_product)

    # Return the maximum product
    return dp[n - 1]

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)