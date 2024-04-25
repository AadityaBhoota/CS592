def is_Sum_Of_Powers_Of_Two(n):
    power_of_2 = 0
    
    while 2**power_of_2 <= n:
        power_of_2 += 1
    
    power_of_2 -= 1  # Move back to the last valid power of 2

    while power_of_2 >= 0:
        if n >= 2**power_of_2:
            n -= 2**power_of_2
            if n == 0:
                return True
        power_of_2 -= 1

    return False

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)