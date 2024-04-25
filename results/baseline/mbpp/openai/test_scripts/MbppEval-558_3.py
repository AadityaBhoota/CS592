def digit_distance_nums(n1, n2):
    str_n1 = str(n1)
    str_n2 = str(n2)
    
    total_distance = 0
    
    for i in range(min(len(str_n1), len(str_n2))):
        digit1 = int(str_n1[i])
        digit2 = int(str_n2[i])
        
        total_distance += abs(digit1 - digit2)
    
    return total_distance

# Test cases




def check(candidate):
    assert digit_distance_nums(1,2) == 1
    assert digit_distance_nums(23,56) == 6
    assert digit_distance_nums(123,256) == 7

check(digit_distance_nums)