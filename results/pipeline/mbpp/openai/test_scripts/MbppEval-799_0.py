def left_rotate(n, d):
    binary = bin(n)[2:].zfill(32)  # Pad with zeros to make it 32-bit
    rotated_binary = binary[d:] + binary[:d]
    return int(rotated_binary, 2)

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