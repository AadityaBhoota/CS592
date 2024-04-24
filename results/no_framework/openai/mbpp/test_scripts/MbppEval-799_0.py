def left_rotate(n, d):
    # Assuming n is a 32-bit number
    num_bits = 32
    # Left shift n by d bits and take only the last 32 bits
    result = ((n << d) | (n >> (num_bits - d))) & ((1 << num_bits) - 1)
    return result

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