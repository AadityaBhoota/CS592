def max_sub_array_sum_repeated(a, n, k):
    max_sum = float('-inf')
    total_sum = sum(a)
    
    if total_sum <= 0:
        return total_sum
    
    max_sum_single = float('-inf')
    current_sum = 0
    
    for i in range(n * k):
        current_sum += a[i % n]
        
        if current_sum > max_sum_single:
            max_sum_single = current_sum
        
        if current_sum < 0:
            current_sum = 0
        
    if k == 1:
        return max_sum_single
    
    max_sum_wrap = float('-inf')
    current_sum = 0
    
    for i in range(n):
        current_sum += a[i]
        
        if current_sum > max_sum_wrap:
            max_sum_wrap = current_sum
        
    return max(max_sum_single, max_sum_single + (k-2) * total_sum + max_sum_wrap)

# Test cases




def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)