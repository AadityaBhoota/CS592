def max_sub_array_sum(a, size):
    max_sum = a[0]
    current_sum = a[0]

    for i in range(1, size):
        current_sum = max(a[i], current_sum + a[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

# Test cases




def check(candidate):
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
    assert max_sub_array_sum([-3, -4, 5, -2, -3, 2, 6, -4], 8) == 8
    assert max_sub_array_sum([-4, -5, 6, -3, -4, 3, 7, -5], 8) == 10

check(max_sub_array_sum)