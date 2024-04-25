def max_product(arr):
    n = len(arr)
    if n < 2:
        return 0

    # Create an array to store the maximum product ending at each index
    dp = [0] * n

    # Initialize the first element of the dp array
    dp[0] = arr[0]

    # Iterate through the array and calculate the max product
    for i in range(1, n):
        max_product = 0
        for j in range(i):
            if arr[i] > arr[j]:
                max_product = max(max_product, dp[j] * arr[i])
        dp[i] = max(dp[i-1], max_product)

    # Return the maximum value in the dp array
    return dp[-1]

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)