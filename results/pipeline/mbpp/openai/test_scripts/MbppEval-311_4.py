def set_left_most_unset_bit(n):
    binary_n = bin(n)[2:]
    
    # Find the position of the leftmost unset bit
    unset_bit_pos = binary_n.rfind('0')

    if unset_bit_pos == -1:
        return n  # If all bits are set, return the input number
    
    # Set the leftmost unset bit to 1
    new_binary = binary_n[:unset_bit_pos] + '1' + binary_n[unset_bit_pos+1:]
    
    return int(new_binary, 2)

def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)