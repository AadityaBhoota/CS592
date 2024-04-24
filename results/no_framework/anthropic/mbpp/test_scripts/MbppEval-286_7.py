def max_sub_array_sum_repeated(a, n, k):
    # Find the maximum subarray sum in the original array
    max_subarray_sum = kadane(a, n)

    # If the maximum subarray sum is negative, return it
    if max_subarray_sum < 0:
        return max_subarray_sum

    # Find the total sum of the original array
    total_sum = sum(a)

    # Calculate the maximum subarray sum in the repeated array
    return max(max_subarray_sum, (k - 1) * total_sum + max_subarray_sum)

def kadane(a, n):
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