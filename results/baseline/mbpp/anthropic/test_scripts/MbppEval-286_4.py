def max_sub_array_sum_repeated(a, n, k):
    # Calculate the sum of the entire array
    total_sum = sum(a)
    
    # If the sum of the entire array is negative, return the maximum element in the array
    if total_sum < 0:
        return max(a)
    
    # Find the maximum subarray sum in the original array
    max_sum = kadane(a, n)
    
    # If the number of repetitions is 1, return the maximum subarray sum
    if k == 1:
        return max_sum
    
    # Calculate the maximum subarray sum in the repeated array
    repeated_max_sum = max_sum * k
    
    # If the sum of the entire array is non-negative, the maximum subarray sum is the maximum of the repeated maximum subarray sum and the sum of the entire array multiplied by the number of repetitions
    return max(repeated_max_sum, total_sum * k)

def kadane(a, n):
    # Kadane's algorithm to find the maximum subarray sum
    max_so_far = a[0]
    max_ending_here = a[0]
    for i in range(1, n):
        max_ending_here = max(a[i], max_ending_here + a[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)