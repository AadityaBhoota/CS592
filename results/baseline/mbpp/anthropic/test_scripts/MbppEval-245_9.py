def max_sum(arr):
    n = len(arr)
    
    # Initialize two arrays to store the maximum sum of the increasing and decreasing subsequences
    increasing = [0] * n
    decreasing = [0] * n
    
    # Compute the maximum sum of the increasing subsequence
    increasing[0] = arr[0]
    for i in range(1, n):
        increasing[i] = max(increasing[i-1] + arr[i], arr[i])
    
    # Compute the maximum sum of the decreasing subsequence
    decreasing[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        decreasing[i] = max(decreasing[i+1] + arr[i], arr[i])
    
    # Find the maximum sum of the bitonic subsequence
    max_sum = 0
    for i in range(n):
        if i == 0:
            max_sum = decreasing[i]
        elif i == n-1:
            max_sum = increasing[i]
        else:
            max_sum = max(max_sum, increasing[i-1] + decreasing[i])
    
    return max_sum

def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)