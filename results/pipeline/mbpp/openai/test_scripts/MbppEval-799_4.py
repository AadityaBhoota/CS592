def left_rotate(n, d):
    binary_n = bin(n)[2:].zfill(32)
    rotated_binary = binary_n[d:] + binary_n[:d]
    result = int(rotated_binary, 2)
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