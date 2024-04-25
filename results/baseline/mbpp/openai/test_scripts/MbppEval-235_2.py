def even_bit_set_number(n): 
    mask = 0xAAAAAAAA  # Mask to set all even bits to 1
    
    result = n | mask  # Set all even bits of n
    
    return result

# Test cases




def check(candidate):
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30

check(even_bit_set_number)