def max_sub_array_sum_repeated(a, n, k):
    # Concatenate the given array 'a' k times
    a_repeated = a * k
    
    max_sum = float('-inf')  # Initialize max_sum as negative infinity
    
    current_sum = 0
    
    for num in a_repeated:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test cases




def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)