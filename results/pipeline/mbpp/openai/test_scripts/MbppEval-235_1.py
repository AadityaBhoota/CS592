def even_bit_set_number(n):
    binary_number = bin(n)[2:].zfill(32)  # Pad the binary number with zeros to have 32 bits

    # Create a mask with all even bits set to 1
    mask = int(''.join(['1' if i % 2 == 0 else '0' for i in range(32)]), 2)
    
    # Perform a bitwise OR operation between the binary number and the mask
    modified_binary = int(binary_number, 2) | mask

    return modified_binary

def check(candidate):
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30

check(even_bit_set_number)