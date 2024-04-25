def max_sub_array_sum_repeated(a, n, k): 
    # Initialize max_sum to the smallest possible integer
    max_sum = float('-inf')

    # Find the maximum sum of contiguous array in the original array
    def max_sub_array_sum(a, n):
        max_sum = float('-inf')
        current_sum = 0
        for i in range(n):
            current_sum = max(a[i], current_sum + a[i])
            max_sum = max(max_sum, current_sum)
        return max_sum

    # Find the maximum sum of the contiguous array in the array repeated k times
    max_sum_original = max_sub_array_sum(a, n)
    max_sum_repeated = max_sub_array_sum(a*min(k, 2), n*k)

    # If the maximum sum in the repeated array comes from within the original array, return that
    if max_sum_repeated < max_sum_original:
        return max_sum_original

    return max_sum_repeated

# Test cases




def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)