def count_Set_Bits(n):
    """
    Write a python function to count the number of set bits (binary digits with value 1) in a given number.

    Examples:
    count_Set_Bits(2) == 1
    count_Set_Bits(4) == 1
    count_Set_Bits(6) == 2
    """
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def check(candidate):
    assert count_Set_Bits(2) == 1
    assert count_Set_Bits(4) == 1
    assert count_Set_Bits(6) == 2

check(count_Set_Bits)