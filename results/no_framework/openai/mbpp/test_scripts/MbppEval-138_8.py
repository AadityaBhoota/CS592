def is_Sum_Of_Powers_Of_Two(n):
    # Convert n to its binary representation
    binary_n = bin(n)[2:]

    # Check if the binary representation contains only one '1'
    if binary_n.count('1') == 1:
        return True
    else:
        return False

# Test cases




def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)