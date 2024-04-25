def highest_Power_of_2(n): 
    return 2**(n.bit_length()-1)

# Test cases




def check(candidate):
    assert highest_Power_of_2(10) == 8
    assert highest_Power_of_2(19) == 16
    assert highest_Power_of_2(32) == 32

check(highest_Power_of_2)