def digit_distance_nums(n1, n2):
    absolute_diff = abs(n1 - n2)
    sum_diff = sum(abs(int(digit1) - int(digit2)) for digit1, digit2 in zip(str(n1), str(n2)))
    
    return sum_diff

def check(candidate):
    assert digit_distance_nums(1,2) == 1
    assert digit_distance_nums(23,56) == 6
    assert digit_distance_nums(123,256) == 7

check(digit_distance_nums)