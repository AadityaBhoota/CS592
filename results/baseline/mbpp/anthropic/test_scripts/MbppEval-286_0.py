def max_sub_array_sum_repeated(a, n, k):
    # Step 1: Calculate the total sum of the array
    total_sum = sum(a)

    # Step 2: Calculate the maximum subarray sum for a single iteration of the array
    max_subarray_sum = float('-inf')
    current_sum = 0
    for i in range(n):
        current_sum = max(a[i], current_sum + a[i])
        max_subarray_sum = max(max_subarray_sum, current_sum)

    # Step 3: Calculate the maximum subarray sum for the repeated array
    if max_subarray_sum >= 0:
        return max(max_subarray_sum * k, total_sum * (k - 1) + max_subarray_sum)
    else:
        return max_subarray_sum * k

def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)