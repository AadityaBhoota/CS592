def set_left_most_unset_bit(n): 
    binary_str = bin(n)[2:]
    unset_bit_index = None
    for i in range(len(binary_str)):
        if binary_str[i] == '1' and (i+1 == len(binary_str) or binary_str[i+1] == '0'):
            unset_bit_index = i
            break

    if unset_bit_index is not None:
        modified_binary = binary_str[:unset_bit_index] + '1' + binary_str[unset_bit_index+1:]
        modified_decimal = int(modified_binary, 2)
        return modified_decimal
    else:
        return n

def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)