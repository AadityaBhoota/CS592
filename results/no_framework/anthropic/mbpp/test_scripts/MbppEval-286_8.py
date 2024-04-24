def max_sub_array_sum_repeated(a, n, k):
    # Compute the total sum of the given array
    total_sum = sum(a)

    # If the total sum is negative, the maximum subarray sum will be the maximum element in the array
    if total_sum < 0:
        return max(a) * k

    # Compute the maximum subarray sum in the given array
    max_sum = kadane(a, n)

    # If the maximum subarray sum is greater than the total sum, then the maximum subarray sum in the repeated array will be the maximum subarray sum in the given array
    if max_sum > total_sum:
        return max_sum * k

    # Otherwise, the maximum subarray sum in the repeated array will be the total sum multiplied by the number of repetitions
    return total_sum * k

def kadane(a, n):
    """
    Compute the maximum subarray sum using Kadane's algorithm.
    """
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