def max_sum(arr):
    n = len(arr)
    if n == 0:
        return 0

    # Calculate the maximum increasing subsequence sum
    increasing = [arr[i] for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                increasing[i] = max(increasing[i], increasing[j] + arr[i])

    # Calculate the maximum decreasing subsequence sum
    decreasing = [arr[i] for i in range(n)]
    for i in range(n - 2, -1, -1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                decreasing[i] = max(decreasing[i], decreasing[j] + arr[i])

    # Find the maximum bitonic subsequence sum
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, increasing[i] + decreasing[i] - arr[i])

    return max_sum

# Test cases




def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)