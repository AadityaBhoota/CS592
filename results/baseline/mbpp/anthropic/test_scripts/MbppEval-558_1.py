def digit_distance_nums(n1, n2):
    """
    Write a python function to find the sum of the per-digit difference between two integers.

    Examples:
    digit_distance_nums(1, 2) == 1
    digit_distance_nums(23, 56) == 6
    digit_distance_nums(123, 256) == 7
    """
    n1_digits = [int(d) for d in str(n1)]
    n2_digits = [int(d) for d in str(n2)]

    max_len = max(len(n1_digits), len(n2_digits))
    n1_digits = [0] * (max_len - len(n1_digits)) + n1_digits
    n2_digits = [0] * (max_len - len(n2_digits)) + n2_digits

    total_distance = 0
    for i in range(max_len):
        total_distance += abs(n1_digits[i] - n2_digits[i])

    return total_distance

def check(candidate):
    assert digit_distance_nums(1,2) == 1
    assert digit_distance_nums(23,56) == 6
    assert digit_distance_nums(123,256) == 7

check(digit_distance_nums)