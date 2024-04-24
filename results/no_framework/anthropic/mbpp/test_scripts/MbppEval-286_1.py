def max_sub_array_sum_repeated(a, n, k):
    # Calculate the total sum of the given array
    total_sum = sum(a)

    # If the total sum is negative and k is odd, return the maximum element
    if total_sum < 0 and k % 2 == 1:
        return max(a)

    # Calculate the maximum subarray sum using Kadane's algorithm
    max_sum = float('-inf')
    current_sum = 0
    for i in range(n * k):
        current_sum = max(a[i % n], current_sum + a[i % n])
        max_sum = max(max_sum, current_sum)

    # If the total sum is non-negative, return the maximum subarray sum multiplied by k
    if total_sum >= 0:
        return max_sum * k
    else:
        # If the total sum is negative, return the maximum subarray sum
        return max_sum

def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)