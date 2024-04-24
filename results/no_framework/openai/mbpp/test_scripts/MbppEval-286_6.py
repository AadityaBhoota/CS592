def max_sub_array_sum_repeated(a, n, k):
    max_sum = float('-inf')
    total_sum = sum(a) * k
    
    if total_sum <= 0:
        return max(a)
    
    for i in range(n):
        current_sum = 0
        for j in range(i, min(i + n*k, n)):
            current_sum += a[j % n]
            max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test the function with examples




def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)