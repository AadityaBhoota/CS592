def left_rotate(n, d):
    # Mask to extract the bits that will be shifted out
    mask = 2**d - 1
    # Extract the bits that will be shifted out
    shifted_out = (n >> (32 - d)) & mask
    # Left shift the number by d bits
    result = ((n << d) | shifted_out)
    return result

# Test the function




def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)