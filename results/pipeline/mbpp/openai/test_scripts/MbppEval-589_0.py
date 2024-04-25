import math

def perfect_squares(a, b):
    result = []
    
    for num in range(a, b+1):
        if math.isqrt(num) ** 2 == num:
            result.append(num)
    
    return result

def check(candidate):
    assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
    assert perfect_squares(50,100)==[64, 81, 100]
    assert perfect_squares(100,200)==[100, 121, 144, 169, 196]

check(perfect_squares)