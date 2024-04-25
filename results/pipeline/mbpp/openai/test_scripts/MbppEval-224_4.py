def count_Set_Bits(n):
    binary = bin(n)[2:]
    count = binary.count('1')
    return count

def check(candidate):
    assert count_Set_Bits(2) == 1
    assert count_Set_Bits(4) == 1
    assert count_Set_Bits(6) == 2

check(count_Set_Bits)