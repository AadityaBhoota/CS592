def left_rotate(n, d):
    def decimal_to_binary_32bit(num):
        return bin(num & 0xFFFFFFFF)[2:].zfill(32)
    
    binary_str = decimal_to_binary_32bit(n)
    rotated_str = binary_str[d:] + binary_str[:d]
    
    return int(rotated_str, 2)

def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)