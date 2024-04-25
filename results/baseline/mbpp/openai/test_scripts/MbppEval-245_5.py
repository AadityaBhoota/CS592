def max_sum(arr):
    n = len(arr)
    if n == 0:
        return 0

    # Initialize two arrays to store increasing and decreasing subsequences
    inc = [0] * n
    dec = [0] * n

    # Initialize the increasing subsequence values as the elements themselves
    for i in range(n):
        inc[i] = arr[i]

    # Find the increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and inc[i] < inc[j] + arr[i]:
                inc[i] = inc[j] + arr[i]

    # Initialize the decreasing subsequence values as the elements themselves
    for i in range(n):
        dec[i] = arr[i]

    # Find the decreasing subsequence
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[i] > arr[j] and dec[i] < dec[j] + arr[i]:
                dec[i] = dec[j] + arr[i]

    max_sum = 0
    # Find the maximum sum by adding the maximum sum of increasing and decreasing subsequences
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i] - arr[i])

    return max_sum

# Test cases




def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)