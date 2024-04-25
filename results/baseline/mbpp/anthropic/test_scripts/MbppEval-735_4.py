def set_middle_bits(n):
    """
    Write a Python function to toggle bits of the number except the first and the last bit.

    Examples:
    set_middle_bits(9) == 15
    set_middle_bits(10) == 12
    set_middle_bits(11) == 13
    """
    # Convert the number to binary string
    binary = bin(n)[2:]

    # Toggle the middle bits (excluding the first and last bits)
    middle_bits = ''.join('1' if bit == '0' else '0' for bit in binary[1:-1])

    # Combine the first and last bits with the toggled middle bits
    new_binary = binary[0] + middle_bits + binary[-1]

    # Convert the new binary string back to an integer
    return int(new_binary, 2)

def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)