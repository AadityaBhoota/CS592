def left_rotate(n, d):
    # Define the 32-bit limit for rotating
    limit = int('1'*32, 2)

    # Left shift n by d bits
    rotated = (n << d) | (n >> (32 - d))

    # Mask with the limit to ensure we are within 32 bits
    rotated = rotated & limit

    return rotated

# Test cases




def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)