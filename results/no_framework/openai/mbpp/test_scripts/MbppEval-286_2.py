def max_sub_array_sum_repeated(a, n, k):
    def kadane(arr):
        max_ending_here = max_so_far = arr[0]
        for i in arr[1:]:
            max_ending_here = max(i, max_ending_here + i)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Apply Kadane's algorithm to the repeated concatenated array
    max_sum = arr_sum = sum(a)
    if max_sum < 0:
        # If the sum of original array is negative, no need to repeat, just return the maximum subarray sum of original array
        return kadane(a)
    for i in range(1, k):
        for num in a:
            a.append(num)
            arr_sum += num
            max_sum = max(max_sum, kadane(a) + max_sum)
        if arr_sum <= 0:
            break

    return max_sum

# Test examples




def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)