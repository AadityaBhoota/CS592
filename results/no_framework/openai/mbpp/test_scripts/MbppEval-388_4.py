def highest_Power_of_2(n): 
    highest_power = 1
    while highest_power * 2 <= n:
        highest_power *= 2
    return highest_power

# Test cases




def check(candidate):
    assert highest_Power_of_2(10) == 8
    assert highest_Power_of_2(19) == 16
    assert highest_Power_of_2(32) == 32

check(highest_Power_of_2)