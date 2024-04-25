def next_power_of_2(n): 
    power_of_2 = 1
    
    if n > 0:
        while power_of_2 < n:
            power_of_2 *= 2
    
    return power_of_2

def check(candidate):
    assert next_power_of_2(0) == 1
    assert next_power_of_2(5) == 8
    assert next_power_of_2(17) == 32

check(next_power_of_2)