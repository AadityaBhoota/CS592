def max_sub_array_sum_repeated(a, n, k):
    # Calculate the total sum of the array
    total_sum = sum(a)

    # If the total sum is negative and k is greater than 1, the answer is the maximum element multiplied by k
    if total_sum < 0 and k > 1:
        return max(a) * k

    # Initialize the maximum subarray sum to the first element of the array
    max_sum = a[0]

    # Compute the maximum subarray sum for the first repetition
    curr_sum = a[0]
    for i in range(1, n):
        curr_sum = max(a[i], curr_sum + a[i])
        max_sum = max(max_sum, curr_sum)

    # Compute the maximum subarray sum for the remaining repetitions
    for _ in range(1, k):
        curr_sum = max_sum
        for i in range(n):
            curr_sum = max(a[i], curr_sum + a[i])
            max_sum = max(max_sum, curr_sum)

    return max_sum

def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)