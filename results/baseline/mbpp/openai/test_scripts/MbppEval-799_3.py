def left_rotate(n, d):
    # Perform the left rotation by shifting to the left by d bits
    # and then transferring the d bits that overflow to the right side.
    return ((n << d) | (n >> (32 - d))) & 0xFFFFFFFF

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