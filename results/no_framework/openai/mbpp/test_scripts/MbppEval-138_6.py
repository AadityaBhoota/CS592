def is_Sum_Of_Powers_Of_Two(n): 
    if n <= 0: 
        return False
    return bin(n).count('1') == 1
  
# Test cases




def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)