def max_sub_array_sum_repeated(a, n, k):
    total_sum = sum(a)
    if total_sum < 0:
        return k * total_sum

    max_sum = float('-inf')
    current_sum = 0
    for i in range(n * k):
        current_sum += a[i % n]
        if i >= n:
            current_sum -= a[(i - n) % n]
        max_sum = max(max_sum, current_sum)

    return max_sum

def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)