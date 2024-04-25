def is_Sum_Of_Powers_Of_Two(n):
    if n == 0:
        return False
    temp = n
    if (temp & (temp - 1)) == 0:
        return True
    while temp:
        if temp & 1 == 1 and not is_Sum_Of_Powers_Of_Two(temp & (temp - 1)):
            return False
        temp >>= 1
    return True

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)