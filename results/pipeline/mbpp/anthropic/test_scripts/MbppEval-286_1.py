def max_sub_array_sum_repeated(a, n, k):
    max_sum = float('-inf')
    total_sum = sum(a)
    
    # Compute the maximum sum of a contiguous subarray in the original array
    curr_sum = 0
    for num in a:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    
    repeated_sum = 0
    for i in range(k-1):
        repeated_sum += total_sum
        max_sum = max(max_sum, repeated_sum)
    
    return max_sum

def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)