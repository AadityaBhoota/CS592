def max_sub_array_sum_repeated(a, n, k):
    # Function to find the maximum subarray sum using Kadane's Algorithm
    def max_sub_array_sum(arr):
        max_sum = float('-inf')
        current_sum = 0

        for num in arr:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

    # Calculate the maximum subarray sum in the original array
    max_sum_original = max_sub_array_sum(a)

    if max_sum_original <= 0:
        return max_sum_original

    # Calculate the sum of the array a
    sum_a = sum(a)

    # Calculate the maximum subarray sum in the modified array
    max_sum_repeated = max_sum_original

    if sum_a > 0:
        max_sum_repeated += sum_a * (k - 1)

    return max_sum_repeated

# Test cases




def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)