def is_Sum_Of_Powers_Of_Two(n): 
    power = 1
    
    while power < n:
        power *= 2
        
    power //= 2
    
    if n == power:
        return True
    elif power > n:
        return False
    else:
        return is_Sum_Of_Powers_Of_Two(n - power)

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)