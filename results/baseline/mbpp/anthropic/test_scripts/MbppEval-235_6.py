def even_bit_set_number(n):
    """
    Write a python function to set all even bits of a given number.

    Examples:
    even_bit_set_number(10) == 10
    even_bit_set_number(20) == 30
    even_bit_set_number(30) == 30
    """
    even_mask = 0xAAAAAAAA  # Binary: 10101010101010101010101010101010
    return n | even_mask

def check(candidate):
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30

check(even_bit_set_number)