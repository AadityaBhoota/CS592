def max_sum(arr):
    n = len(arr)
    if n < 2:
        return 0

    # Initialize two arrays to store the increasing and decreasing sequences
    inc = [0] * n
    dec = [0] * n

    # Compute the increasing sequence
    inc[0] = arr[0]
    for i in range(1, n):
        inc[i] = max(inc[i-1] + arr[i], arr[i])

    # Compute the decreasing sequence
    dec[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        dec[i] = max(dec[i+1] + arr[i], arr[i])

    # Find the maximum sum of a bitonic subsequence
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i] - arr[i])

    return max_sum

def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)