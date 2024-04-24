def is_Sum_Of_Powers_Of_Two(n):
    # Convert n to binary and remove the leading '0b'
    binary = bin(n)[2:]
    
    # Check if the binary representation has only one '1'
    if binary.count('1') == 1:
        return True
    else:
        return False

# Test the function




def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)