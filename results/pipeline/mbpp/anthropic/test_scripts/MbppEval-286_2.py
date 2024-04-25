def max_sub_array_sum_repeated(a, n, k):
    max_subarray_sum = float('-inf')
    total_sum = 0
    
    # Calculate the total sum of the original array
    for num in a:
        total_sum += num
    
    # Find the maximum subarray sum in the original array
    curr_sum = 0
    for num in a:
        curr_sum = max(num, curr_sum + num)
        max_subarray_sum = max(max_subarray_sum, curr_sum)
    
    # Calculate the maximum subarray sum in the repeated array
    if total_sum >= 0:
        return max_subarray_sum * k
    else:
        return max(max_subarray_sum, max_subarray_sum + (k - 1) * total_sum)

def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)