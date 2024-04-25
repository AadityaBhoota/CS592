def digit_distance_nums(n1, n2):
    n1_str = str(n1)
    n2_str = str(n2)
    total_distance = 0
    for i in range(max(len(n1_str), len(n2_str))):
        d1 = int(n1_str[i]) if i < len(n1_str) else 0
        d2 = int(n2_str[i]) if i < len(n2_str) else 0
        total_distance += abs(d1 - d2)
    return total_distance

def check(candidate):
    assert digit_distance_nums(1,2) == 1
    assert digit_distance_nums(23,56) == 6
    assert digit_distance_nums(123,256) == 7

check(digit_distance_nums)