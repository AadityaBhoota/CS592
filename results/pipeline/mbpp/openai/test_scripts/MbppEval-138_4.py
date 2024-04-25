def is_Sum_Of_Powers_Of_Two(n): 
    if n < 1:
        return False
    
    while n > 1:
        if n % 2 != 0:
            return False
        n = n / 2
    
    return n == 1

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)