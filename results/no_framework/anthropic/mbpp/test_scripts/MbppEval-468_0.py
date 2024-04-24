def max_product(arr):
    n = len(arr)
    if n == 0:
        return 0

    # Create a dp array to store the maximum product up to each index
    dp = [1] * n

    # Iterate through the array, updating the dp array
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] * arr[i])

    # Return the maximum value in the dp array
    return max(dp)

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)