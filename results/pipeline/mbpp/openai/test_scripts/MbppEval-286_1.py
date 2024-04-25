def max_sub_array_sum_repeated(a, n, k):
    repeated_array = a * (k - 1) + a  # Repeat (k-1) times and add the original array once
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    
    # Loop through all possible subarrays of length n
    for i in range(len(repeated_array) - n + 1):
        current_sum = sum(repeated_array[i:i+n])
        max_sum = max(max_sum, current_sum)

    return max_sum

def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)