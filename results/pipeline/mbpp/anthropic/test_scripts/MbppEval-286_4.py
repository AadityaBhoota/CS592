def max_sub_array_sum_repeated(a, n, k):
    # Step 1: Use Kadane's algorithm to find the maximum subarray sum in the original array
    max_subarray_sum = float('-inf')
    current_sum = 0
    for num in a:
        current_sum = max(num, current_sum + num)
        max_subarray_sum = max(max_subarray_sum, current_sum)

    # Step 2: Calculate the total sum of the array
    total_sum = sum(a)

    # Step 3: If the maximum subarray sum is negative, return the maximum subarray sum
    if max_subarray_sum < 0:
        return max_subarray_sum

    # Step 4: Calculate the maximum subarray sum in the repeated array
    return max_subarray_sum + (total_sum * (k - 1))

def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)