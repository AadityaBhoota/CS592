def max_sum(arr): 
    n = len(arr)
    lis = [0] * n 
    lds = [0] * n
  
    for i in range(n): 
        lis[i] = arr[i] 
        lds[i] = arr[i] 
  
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + arr[i])
  
    for i in reversed(range(n - 1)):
        for j in reversed(range(i - 1, n)):
            if arr[i] > arr[j]:
                lds[i] = max(lds[i], lds[j] + arr[i])
  
    max_val = 0
    for i in range(n):
        if lis[i] + lds[i] - arr[i] > max_val:
            max_val = lis[i] + lds[i] - arr[i]
  
    return max(max_val, max(lis), max(lds))

# Examples




def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)