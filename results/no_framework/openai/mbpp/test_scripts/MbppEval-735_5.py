def set_middle_bits(n):
    if n < 3:
        return n

    # Extracting the first and last bit of the number
    first_bit = n & 1
    last_bit = n & (1 << (n.bit_length() - 1))

    # Toggling the bits except the first and last bit
    mask = (1 << (n.bit_length() - 2)) - 1
    middle_bits = n & mask
    toggled_middle_bits = middle_bits ^ mask

    # Combining the first bit, toggled middle bits, and last bit to get the final result
    result = first_bit | toggled_middle_bits | last_bit
    
    return result

# Test Cases




def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)