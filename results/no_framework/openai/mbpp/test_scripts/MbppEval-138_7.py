def is_Sum_Of_Powers_Of_Two(n):
    # Check if the number is a power of 2
    if n & (n-1) == 0:
        return False
    
    # Convert the number into binary representation
    binary_str = bin(n)[2:]
    
    # Check if there is only one '1' bit in the binary representation
    if binary_str.count('1') == 1:
        return False
    
    return True

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)