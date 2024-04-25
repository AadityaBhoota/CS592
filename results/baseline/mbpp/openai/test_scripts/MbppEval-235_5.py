def even_bit_set_number(n):
    even_set_bits = 0
    i = 0
    
    while n:
        if i % 2 == 0:
            even_set_bits |= n & 1
        n >>= 1
        i += 1
    
    return even_set_bits

# Test cases




def check(candidate):
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30

check(even_bit_set_number)