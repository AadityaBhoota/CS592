def max_sub_array_sum(a, size):
    max_so_far = a[0]
    max_ending_here = a[0]

    for i in range(1, size):
        max_ending_here = max(a[i], max_ending_here + a[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

def check(candidate):
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
    assert max_sub_array_sum([-3, -4, 5, -2, -3, 2, 6, -4], 8) == 8
    assert max_sub_array_sum([-4, -5, 6, -3, -4, 3, 7, -5], 8) == 10

check(max_sub_array_sum)