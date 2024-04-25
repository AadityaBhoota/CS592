def max_sum(arr):
    n = len(arr)
    increasing = [0] * n
    decreasing = [0] * n

    # Calculate the increasing part
    increasing[0] = arr[0]
    for i in range(1, n):
        increasing[i] = max(arr[i], increasing[i-1] + arr[i])

    # Calculate the decreasing part
    decreasing[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        decreasing[i] = max(arr[i], decreasing[i+1] + arr[i])

    max_val = 0
    for i in range(n):
        max_val = max(max_val, increasing[i] + decreasing[i] - arr[i])

    return max_val

def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)