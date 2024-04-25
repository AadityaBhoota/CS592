def even_bit_set_number(n):
    mask = 0b10101010101010101010101010101010
    result = n | mask
    return result

def check(candidate):
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30

check(even_bit_set_number)