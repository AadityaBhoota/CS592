def highest_Power_of_2(n): 
    power_of_2 = 1

    while power_of_2 * 2 <= n:
        power_of_2 *= 2

    return power_of_2

def check(candidate):
    assert highest_Power_of_2(10) == 8
    assert highest_Power_of_2(19) == 16
    assert highest_Power_of_2(32) == 32

check(highest_Power_of_2)