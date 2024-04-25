def is_Sum_Of_Powers_Of_Two(n): 
    if n < 1:
        return False
    
    for i in range(n, 0, -1):
        if 2**i <= n:
            n -= 2**i
            if n == 0:
                return True
    
    return False

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)