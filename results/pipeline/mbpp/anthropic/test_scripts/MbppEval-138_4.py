def is_Sum_Of_Powers_Of_Two(n):
    temp = n
    result = True
    
    i = 1
    while i <= n:
        if temp >= i:
            if temp % i == 0:
                temp -= i
            else:
                result = False
        i *= 2
    
    return result

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)