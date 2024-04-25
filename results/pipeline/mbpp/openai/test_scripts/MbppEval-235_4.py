def even_bit_set_number(n):
    # Using a 32-bit integer mask to set all even bits to 1
    even_bits_mask = 0xAAAAAAAA
    
    result = n | even_bits_mask
    return result

# Test cases




def check(candidate):
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30

check(even_bit_set_number)