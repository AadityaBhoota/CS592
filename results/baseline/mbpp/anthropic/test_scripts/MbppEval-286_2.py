def max_sub_array_sum_repeated(a, n, k):
    total_sum = sum(a)
    max_sum = float('-inf')
    curr_sum = 0

    for i in range(n * k):
        curr_sum += a[i % n]
        max_sum = max(max_sum, curr_sum)

        if curr_sum < 0:
            curr_sum = 0

    # If the array contains only negative numbers, return the maximum element
    if max_sum == float('-inf'):
        return max(a)

    # If the array contains only positive numbers, return the sum of the array multiplied by k
    if total_sum > 0:
        return total_sum * k

    return max_sum

def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)