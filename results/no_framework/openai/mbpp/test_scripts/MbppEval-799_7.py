def left_rotate(n, d):
    # Define the number of bits
    num_bits = 32
    
    # Mask to select the leftmost d bits
    mask = (1 << d) - 1
    
    # Extract the leftmost d bits from the number
    left_bits = (n >> (num_bits - d)) & mask
    
    # Left shift the original number by d bits
    result = (n << d) % (1 << num_bits)
    
    # Append the extracted leftmost bits to the result
    result |= left_bits
    
    return result

def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)