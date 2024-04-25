def max_sub_array_sum_repeated(a, n, k):
    # Step 1: Concatenate the given array a k times to form the modified array
    modified_array = a * k
    
    # Step 2: Find the largest sum of a contiguous subarray
    max_sum = current_sum = modified_array[0]
    
    for num in modified_array[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test the function


def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)