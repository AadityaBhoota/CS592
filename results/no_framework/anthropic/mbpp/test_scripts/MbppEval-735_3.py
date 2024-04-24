def set_middle_bits(n):
    """
    Write a python function to toggle bits of the number except the first and the last bit.
    Examples:
    set_middle_bits(9) == 15
    set_middle_bits(10) == 12
    set_middle_bits(11) == 13
    """
    # Convert the number to binary string
    binary_str = bin(n)[2:]

    # Reverse the binary string
    reversed_binary_str = binary_str[::-1]

    # Toggle the middle bits (except the first and last bit)
    toggled_binary_str = reversed_binary_str[1:-1]
    toggled_binary_str = ''.join(['1' if bit == '0' else '0' for bit in toggled_binary_str])

    # Reverse the toggled binary string and convert it back to decimal
    result = int(toggled_binary_str[::-1], 2)

    return result

def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)