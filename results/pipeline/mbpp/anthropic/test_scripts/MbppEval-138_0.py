def is_Sum_Of_Powers_Of_Two(n):
    power = 0
    sum_of_powers = 0
    
    while 2 ** power <= n:
        sum_of_powers += 2 ** power
        power += 1
    
    return sum_of_powers == n

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)