def even_bit_set_number(n): 
    return n | 0b1010101010101010

# Test cases




def check(candidate):
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30

check(even_bit_set_number)