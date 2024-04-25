def even_bit_set_number(n):
    # Create a mask with even bits set to 1 (1010...)
    mask = 0xAAAAAAAA

    # Perform bitwise OR operation to set even bits of n
    result = n | mask

    return result

# Test cases




def check(candidate):
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30

check(even_bit_set_number)