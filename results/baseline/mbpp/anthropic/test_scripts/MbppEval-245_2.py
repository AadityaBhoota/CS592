def max_sum(arr):
    """
    Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.

    Examples:
    max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9], 9) == 194
    max_sum([80, 60, 30, 40, 20, 10], 6) == 210
    max_sum([2, 3, 14, 16, 21, 23, 29, 30], 8) == 138
    """
    n = len(arr)
    if n < 2:
        return sum(arr)

    # Create two arrays to store the maximum sum of increasing and decreasing subsequences
    inc_sum = [0] * n
    dec_sum = [0] * n

    # Compute the maximum sum of increasing subsequences
    inc_sum[0] = arr[0]
    for i in range(1, n):
        inc_sum[i] = max(inc_sum[i-1], inc_sum[i-1] + arr[i])

    # Compute the maximum sum of decreasing subsequences
    dec_sum[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        dec_sum[i] = max(dec_sum[i+1], dec_sum[i+1] + arr[i])

    # Find the maximum sum of a bitonic subsequence
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, inc_sum[i] + dec_sum[i] - arr[i])

    return max_sum

def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)