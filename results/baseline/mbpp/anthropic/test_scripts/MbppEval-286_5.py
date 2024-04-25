def max_sub_array_sum_repeated(a, n, k):
    """
    Find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
    """
    total_sum = sum(a)
    max_sum = float('-inf')
    current_sum = 0

    for i in range(n * k):
        current_sum += a[i % n]
        max_sum = max(max_sum, current_sum)

        if current_sum < 0:
            current_sum = 0

    if total_sum < 0 and k > 1:
        return k * total_sum
    else:
        return max_sum

def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)