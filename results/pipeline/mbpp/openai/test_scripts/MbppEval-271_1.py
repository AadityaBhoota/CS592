def even_Power_Sum(n):
    sum_even_power = 0
    even_number = 2
    
    for _ in range(n):
        sum_even_power += even_number**5
        even_number += 2
        
    return sum_even_power

def check(candidate):
    assert even_Power_Sum(2) == 1056
    assert even_Power_Sum(3) == 8832
    assert even_Power_Sum(1) == 32

check(even_Power_Sum)