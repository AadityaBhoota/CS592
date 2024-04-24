def highest_Power_of_2(n): 
    power = 0
    while 2**power <= n:
        power += 1
    return 2**(power-1)

# Test cases




def check(candidate):
    assert highest_Power_of_2(10) == 8
    assert highest_Power_of_2(19) == 16
    assert highest_Power_of_2(32) == 32

check(highest_Power_of_2)