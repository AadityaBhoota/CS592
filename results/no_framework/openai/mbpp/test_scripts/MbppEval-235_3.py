def even_bit_set_number(n):
    mask = 0xAAAAAAAA  # 0xAAAAAAAA represents the number with all even bits set to 1 (1010 1010 ...)

    result = n | mask  # Set even bits of n by performing bitwise OR with the mask

    return result

# Test cases




def check(candidate):
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30

check(even_bit_set_number)