def digit_distance_nums(n1, n2):
    sum_diff = 0
    n1_str = str(n1)
    n2_str = str(n2)
    
    min_len = min(len(n1_str), len(n2_str))
    
    sum_diff = 0
    
    for i in range(min_len):
        digit_diff = abs(int(n1_str[i]) - int(n2_str[i]))
        sum_diff += digit_diff
        
    if len(n1_str) > len(n2_str):
        for i in range(min_len, len(n1_str)):
            sum_diff += int(n1_str[i])
    elif len(n2_str) > len(n1_str):
        for i in range(min_len, len(n2_str)):
            sum_diff += int(n2_str[i])
    
    return sum_diff

def check(candidate):
    assert digit_distance_nums(1,2) == 1
    assert digit_distance_nums(23,56) == 6
    assert digit_distance_nums(123,256) == 7

check(digit_distance_nums)