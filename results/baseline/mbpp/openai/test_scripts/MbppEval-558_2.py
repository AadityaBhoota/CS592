def digit_distance_nums(n1, n2):
    sum_distance = 0
    
    while n1 > 0 or n2 > 0:
        digit_n1 = n1 % 10
        digit_n2 = n2 % 10
        
        sum_distance += abs(digit_n1 - digit_n2)
        
        n1 //= 10
        n2 //= 10
    
    return sum_distance

# Test cases
assert digit_distance_nums(1, 2) == 1
assert digit_distance_nums(23, 56) == 6
assert digit_distance_nums(123, 256) == 7

def check(candidate):
    assert digit_distance_nums(1,2) == 1
    assert digit_distance_nums(23,56) == 6
    assert digit_distance_nums(123,256) == 7

check(digit_distance_nums)