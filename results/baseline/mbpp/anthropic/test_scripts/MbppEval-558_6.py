def digit_distance_nums(n1, n2):
    """
    Write a python function to find the sum of the per-digit difference between two integers.

    Examples:
    digit_distance_nums(1, 2) == 1
    digit_distance_nums(23, 56) == 6
    digit_distance_nums(123, 256) == 7
    """
    n1_str = str(n1)
    n2_str = str(n2)

    # Ensure the numbers have the same number of digits
    max_length = max(len(n1_str), len(n2_str))
    n1_str = n1_str.zfill(max_length)
    n2_str = n2_str.zfill(max_length)

    total_distance = 0
    for i in range(max_length):
        total_distance += abs(int(n1_str[i]) - int(n2_str[i]))

    return total_distance

def check(candidate):
    assert digit_distance_nums(1,2) == 1
    assert digit_distance_nums(23,56) == 6
    assert digit_distance_nums(123,256) == 7

check(digit_distance_nums)