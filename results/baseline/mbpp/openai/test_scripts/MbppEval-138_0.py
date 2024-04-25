def is_Sum_Of_Powers_Of_Two(n):
    if n <= 0:
        return False
    
    binary_rep = bin(n)[2:]
    return '1' in binary_rep[1:]

# Test cases




def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)