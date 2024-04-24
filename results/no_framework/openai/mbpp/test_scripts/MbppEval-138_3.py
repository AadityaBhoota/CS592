def is_Sum_Of_Powers_Of_Two(n):
    if n <= 0:
        return False
    binary_repr = bin(n)[2:]
    return '1' in binary_repr[1:] and all(bit == '0' for bit in binary_repr[1:])

# Test cases




def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)