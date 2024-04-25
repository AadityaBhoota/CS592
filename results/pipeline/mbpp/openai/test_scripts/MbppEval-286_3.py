def max_sub_array_sum_repeated(a, n, k): 
    modified_array = a * k
    max_sum = float('-inf')
    
    # Iterate over all possible subarrays of length n
    for i in range(len(modified_array) - n + 1):
        current_sum = sum(modified_array[i:i+n])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)