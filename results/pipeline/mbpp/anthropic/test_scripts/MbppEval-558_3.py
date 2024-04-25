def digit_distance_nums(n1, n2):
    max_len = max(len(str(n1)), len(str(n2)))
    n1_str = str(n1).zfill(max_len)
    n2_str = str(n2).zfill(max_len)
    total_distance = 0
    for i in range(max_len):
        total_distance += abs(int(n1_str[i]) - int(n2_str[i]))
    return total_distance

def check(candidate):
    assert digit_distance_nums(1,2) == 1
    assert digit_distance_nums(23,56) == 6
    assert digit_distance_nums(123,256) == 7

check(digit_distance_nums)