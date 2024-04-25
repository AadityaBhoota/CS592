def highest_Power_of_2(n):
    power = 0
    while n >= 2:
        n //= 2
        power += 1
    return 2 ** power

def check(candidate):
    assert highest_Power_of_2(10) == 8
    assert highest_Power_of_2(19) == 16
    assert highest_Power_of_2(32) == 32

check(highest_Power_of_2)