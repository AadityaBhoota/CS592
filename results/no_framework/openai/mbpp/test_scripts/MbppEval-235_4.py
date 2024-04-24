def even_bit_set_number(n):
    # Mask to set all even bits to 1: 1010 1010 1010 ...
    mask = 0xAAAAAAAA
    
    # Perform bitwise OR operation with the mask to set all even bits of the given number
    result = n | mask
    
    return result

# Test cases




def check(candidate):
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30

check(even_bit_set_number)