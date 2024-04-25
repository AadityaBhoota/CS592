import math

def is_ludic(num):
    if num == 1:
        return True
    if num % 2 == 0:
        return True
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True

def get_ludic(n):
    ludic_numbers = []
    
    for num in range(1, n+1):
        if is_ludic(num):
            ludic_numbers.append(num)
    
    return ludic_numbers

def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]

check(get_ludic)