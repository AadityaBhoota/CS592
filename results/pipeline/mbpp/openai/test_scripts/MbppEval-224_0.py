def count_Set_Bits(n):
    count = 0
    binary_str = bin(n)[2:]
    
    for digit in binary_str:
        if digit == '1':
            count += 1
            
    return count

def check(candidate):
    assert count_Set_Bits(2) == 1
    assert count_Set_Bits(4) == 1
    assert count_Set_Bits(6) == 2

check(count_Set_Bits)