def is_Sum_Of_Powers_Of_Two(n): 
    if n <= 0:
        return False
    
    power = 1
    while power <= n:
        if n % power != 0:
            power *= 2

            if power > n:
                return False

    return True

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)