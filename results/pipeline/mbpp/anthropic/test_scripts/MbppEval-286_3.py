def max_sub_array_sum_repeated(a, n, k):
    max_sum = float('-inf')
    current_sum = 0
    min_sum = 0
    total_sum = 0

    for _ in range(k):
        current_sum = max(current_sum + a[i], a[i])
        max_sum = max(max_sum, current_sum)
        min_sum = min(min_sum, current_sum)
        total_sum += a[i]
        i = (i + 1) % n

    # If all elements are negative, return the maximum element
    if max_sum < 0:
        return max_sum

    return max(max_sum, total_sum - min_sum)

def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)