def max_product(arr):
    """
    Finds the maximum product formed by multiplying numbers of an increasing subsequence of the given array.

    Args:
        arr (list): The input array.

    Returns:
        int: The maximum product.
    """
    n = len(arr)
    dp = [1] * n  # Initialize the dynamic programming array
    max_prod = 1

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] * arr[i])
        max_prod = max(max_prod, dp[i])

    return max_prod

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)