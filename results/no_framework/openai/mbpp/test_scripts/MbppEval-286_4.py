def max_sub_array_sum_repeated(a, n, k):
    max_sum = a[0]
    current_sum = a[0]
    
    for i in range(1, n*k):
        current_sum = max(a[i % n], current_sum + a[i % n])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test the function with the given examples




def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)