def left_rotate(n, d):
    # Assuming the number is 32 bit
    bits = 32
    
    # Mask for 32 bit number
    mask = (1 << bits) - 1
    
    # Left shift by d bits and wrap around
    result = (n << d) | (n >> (bits - d))
    
    # Apply mask to get the desired 32 bits result
    result = result & mask
    
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