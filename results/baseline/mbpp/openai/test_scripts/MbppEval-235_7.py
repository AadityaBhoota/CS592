def even_bit_set_number(n):
    mask = 0xAAAAAAAA  # Mask with even bits set to 1 (1010 1010 1010 1010)
    result = n | mask  # Setting even bits of the number using bitwise OR

    return result

def check(candidate):
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30

check(even_bit_set_number)